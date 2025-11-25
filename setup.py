#!/usr/bin/env python

from setuptools import find_packages, setup

import os
import subprocess
import time

version_file = 'gfpgan/version.py'
version_txt = 'VERSION'  # 新增：单独记录版本号的文件路径


def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content


def get_git_hash():

    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH', 'HOME']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        sha = out.strip().decode('ascii')
    except OSError:
        sha = 'unknown'

    return sha


def get_hash():
    if os.path.exists('.git'):
        sha = get_git_hash()[:7]
    else:
        sha = 'unknown'

    return sha


def write_version_py():
    """根据 VERSION 文件生成 gfpgan/version.py"""
    content = """# GENERATED VERSION FILE
# TIME: {}
__version__ = '{}'
__gitsha__ = '{}'
version_info = ({})
"""
    sha = get_hash()
    with open(version_txt, 'r', encoding='utf-8') as f:
        SHORT_VERSION = f.read().strip()
    VERSION_INFO = ', '.join([x if x.isdigit() else f'"{x}"' for x in SHORT_VERSION.split('.')])

    version_file_str = content.format(time.asctime(), SHORT_VERSION, sha, VERSION_INFO)
    os.makedirs(os.path.dirname(version_file), exist_ok=True)
    with open(version_file, 'w', encoding='utf-8') as f:
        f.write(version_file_str)


def get_version():
    """在 PEP 517 / build_meta 场景下安全获取版本号"""

    # 1. 如果 VERSION 文件存在，且 version.py 不存在，则先生成 version.py
    if os.path.exists(version_txt) and not os.path.exists(version_file):
        write_version_py()

    # 2. 优先从 version.py 读取 __version__
    if os.path.exists(version_file):
        about = {}
        with open(version_file, 'r', encoding='utf-8') as f:
            # 注意：把字典显式传给 exec，避免原来的 locals()['__version__'] 问题
            exec(f.read(), about)
        if "__version__" in about:
            return about["__version__"]

    # 3. 退而求其次：直接从 VERSION 文件读
    if os.path.exists(version_txt):
        with open(version_txt, 'r', encoding='utf-8') as f:
            return f.read().strip()

    # 4. 实在不行给一个兜底版本，避免 KeyError 直接炸掉构建
    return "0.0.0"


def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r', encoding='utf-8') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires


if __name__ == '__main__':
    # 这里保留原来的行为：作为脚本执行时，会先写 version.py
    if os.path.exists(version_txt):
        write_version_py()

    setup(
        name='gfpgan',
        version=get_version(),
        description='GFPGAN aims at developing Practical Algorithms for Real-world Face Restoration',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author='Xintao Wang',
        author_email='xintao.wang@outlook.com',
        keywords='computer vision, pytorch, image restoration, super-resolution, face restoration, gan, gfpgan',
        url='https://github.com/TencentARC/GFPGAN',
        include_package_data=True,
        packages=find_packages(exclude=('options', 'datasets', 'experiments', 'results', 'tb_logger', 'wandb')),
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
        license='Apache License Version 2.0',
        setup_requires=['cython', 'numpy'],
        install_requires=get_requirements(),
        zip_safe=False)