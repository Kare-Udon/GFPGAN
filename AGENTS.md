# Agent Notes
- Torchvision compatibility: `gfpgan/torchvision_compat.ensure_legacy_torchvision_support` shims the removed `torchvision.transforms.functional_tensor`. Call it before any new Basicsr imports in future entrypoints.
- Patched entrypoints: `inference_gfpgan.py`, `cog_predict.py`, `scripts/parse_landmark.py`, and `gfpgan/train.py` already invoke the shim; mirror this pattern in new scripts.
- Testing: quick verification uses `PYTHONPATH=. pytest tests/test_torchvision_compat.py -o addopts=`. Running the full suite still requires installing Basicsr, cv2, and other heavy deps.
- Dependencies: `requirements.txt` now includes `pytest` for the compatibility test; install with your preferred environment tool (uv/pip/conda). 
