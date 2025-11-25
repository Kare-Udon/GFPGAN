# 常用命令
- 安装依赖（基础）：`pip install -r requirements.txt && python setup.py develop`（或用 uv/pip/conda 等同配置）。
- 推理示例：`python inference_gfpgan.py -i inputs/whole_imgs -o results -v 1.3 -s 2`。
- 兼容补丁验证：`PYTHONPATH=. pytest tests/test_torchvision_compat.py -o addopts=`（需已安装 pytest）。
- 训练入口：`python gfpgan/train.py`（需准备配置和训练数据）。
- 格式化/检查：`yapf -i <file>`，`flake8 <paths>`（行宽 120）。