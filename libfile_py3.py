# -*- coding: utf-8 -*-
"""
author : Comet
modified time : 2019-9-8
"""

import sys
import os
import pathlib
import fnmatch
import glob


def mkdir(directory):
    if not isinstance(directory, pathlib.PurePath):
        directory = pathlib.Path(directory)
    if directory.is_file():
        print("{} 是文件路径".format(directory))
        # sys.exit(0)
        return False
    else:
        if directory.exists():
            # print("{} 目录已存在".format(path))
            return True
        else:
            directory.mkdir(exist_ok=True, parents=True)
            # print("{} 创建成功".format(path))
            return True


def searchdir(source, pattern='*', recursive=False):
    if not isinstance(source, pathlib.PurePath):
        source = pathlib.Path(source)
    if source.is_dir() and source.exists():
        if recursive:
            res = list(source.rglob(pattern))
        else:
            res = list(source.glob(pattern))
    else:
        print("{} is a file path or folder path is not exists!".format(source))
        return False
    dirlist = [i for i in res if i.is_dir()]
    return dirlist


def searchfile(source, pattern='*', recursive=False):
    if not isinstance(source, pathlib.PurePath):
        source = pathlib.Path(source)
    if source.is_dir() and source.exists():
        if recursive:
            res = list(source.rglob(pattern))
        else:
            res = list(source.glob(pattern))
    else:   
        print("{} is a file path or folder path is not exists!".format(source))
        return False
    filelist = [i for i in res if i.is_file()]
    return filelist
 