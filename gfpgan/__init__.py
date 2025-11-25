"""GFPGAN包初始化，按需补齐兼容补丁。"""
# flake8: noqa
from .torchvision_compat import ensure_legacy_torchvision_support

ensure_legacy_torchvision_support()

from .archs import *
from .data import *
from .models import *
from .utils import *

# from .version import *
