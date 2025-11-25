import sys


def ensure_legacy_torchvision_support() -> None:
    """为新版torchvision补齐被移除的functional_tensor路径。"""
    target_module = "torchvision.transforms.functional_tensor"
    if target_module in sys.modules:
        return
    try:
        import torchvision.transforms.functional as functional
    except Exception:
        return

    # 使用公开的functional模块填充Basicsr仍在引用的旧路径
    sys.modules[target_module] = functional
    try:
        import torchvision.transforms as transforms
        if not hasattr(transforms, "functional_tensor"):
            transforms.functional_tensor = functional
    except Exception:
        pass
