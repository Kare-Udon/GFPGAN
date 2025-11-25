# 项目概览
- 目标：GFPGAN 实现人脸修复/超分，基于 StyleGAN2 先验，提供推理脚本、训练代码和预训练权重下载。
- 技术栈：Python 3.7+，PyTorch 1.7+，torchvision，BasicSR、facexlib、Real-ESRGAN 等；使用 setuptools 安装。
- 目录结构：
  - `gfpgan/` 核心包，包含 `archs/`、`models/`、`data/`、`utils/`、`train.py` 等。
  - `inference_gfpgan.py`、`cog_predict.py`、`scripts/parse_landmark.py` 等入口脚本。
  - `experiments/pretrained_models`、`assets`、`inputs`、`tests/` 等辅助资源。
- 运行方式：可直接用仓库根目录执行推理脚本；模型权重默认放在 `experiments/pretrained_models/` 或 `gfpgan/weights/`。
- 近期修改：新增 torchvision 兼容补丁 `gfpgan/torchvision_compat.py` 并在主要入口调用。