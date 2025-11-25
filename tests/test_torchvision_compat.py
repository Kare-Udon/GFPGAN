import importlib
import importlib.util
from pathlib import Path
import sys


def _load_module():
    path = Path(__file__).resolve().parent.parent / "gfpgan" / "torchvision_compat.py"
    spec = importlib.util.spec_from_file_location("gfpgan.torchvision_compat", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_functional_tensor_alias(monkeypatch):
    """确保新版torchvision仍可通过旧路径导入必要函数。"""
    module = _load_module()
    target = "torchvision.transforms.functional_tensor"
    monkeypatch.delitem(sys.modules, target, raising=False)
    module.ensure_legacy_torchvision_support()
    module = importlib.import_module(target)
    assert hasattr(module, "rgb_to_grayscale")
