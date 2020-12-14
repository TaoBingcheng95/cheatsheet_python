#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import print_function
import platform
import sys
import os
import pathlib
# import pprint
import psutil
import math
"""
global var
是否显示日志信息
"""
SHOW_LOG = True


def main():
    init()
    test()
    return None


def init():
    global SHOW_LOG
    SHOW_LOG = True
    return None


def test():
    # with open('sys_info.txt', 'w') as writer:
    print("操作系统信息:")  # , file=writer
    print("操作系统 : [{}]\n{}".format(sys.platform, "-" * 20))

    if SHOW_LOG:
        show_os_info()  # writer

    print("{}".format("-" * 20))

    print("Python信息：")
    if sys.version > '3':
        print("Python3\n{}".format("-" * 20))
    else:
        print("Python2\n{}".format("-" * 20))

    if SHOW_LOG:
        show_python_info()

    print("{}".format("-" * 20))

    if SHOW_LOG:
        print("环境变量信息:")
        print("Language : [{}]".format(os.getenv('LANG')))
        print("HOME : [{}]".format(os.getenv('HOME')))
        print("USER : [{}]".format(os.getenv('USER')))
        print("HOSTNAME : [{}]".format(os.getenv('HOSTNAME')))
        print("SHELL : [{}]".format(os.getenv('SHELL')))

        print("Print environ info :/n{}".format("-" * 20))
        for key in os.environ:
            print(key, os.environ[key])

    return None


def show_python_info():
    """打印python的全部信息"""
    print("Python System Version: [{}]".format(sys.version))
    print("System Version Info: [{}]".format(sys.version_info))
    print("The Python version as tuple (major, minor, patch_level) : [{}]".
          format(platform.python_version_tuple()))
    print("The version of python: [{}]".format(platform.python_version()))
    # Returns the Python version as string 'major.minor.patch_level'
    print("The Python build number and date : [{}]".format(
        platform.python_build()))
    print("The compiler used for compiling Python : [{}]".format(
        platform.python_compiler()))
    print("The Python implementation SCM branch : [{}]".format(
        platform.python_branch()))
    print("Python implementation SCM revision : [{}]".format(
        platform.python_revision()))
    print("The Python implementation : [{}]".format(
        platform.python_implementation()))
    return None


def show_os_info():
    """打印os的全部信息"""
    print("操作系统类型 : [{}]".format(platform.system()))
    print("操作系统名称及版本号 : [{}]".format(platform.platform()))
    print("操作系统版本号 : [{}]".format(platform.version()))
    print("操作系统架构 : [{}]".format(platform.architecture()))
    print("计算机网络名称 : [{}]".format(platform.node()))
    print("CPU平台类型 : [{}]".format(platform.machine()))
    print("CPU处理器信息 : [{}]".format(platform.processor()))
    # print("汇总信息 : [{}]".format(platform.uname()), file=f)
    return None


if __name__ == '__main__':

    print("program begin!\n{}".format("-" * 20))

    print("cwd: {}".format(os.getcwd()))
    pwd = pathlib.Path.cwd()
    # print(pwd)
    print("father dir: {}".format(pwd.parent))
    print("grandfather dir: {}".format(pwd.parent.parent))
    print("{}".format("-" * 20))

    main()
    '''获取内存信息'''
    mem = psutil.virtual_memory()
    # print(type(mem))
    print("内存信息： {}".format(mem))
    print("总内存数： {}".format(mem.total))
    print("闲置内存： {}".format(mem.free))
    print("SWAP分区信息: {}".format(psutil.swap_memory()))
    print("{}".format("-" * 20))
    '''获取CPU信息'''
    print("CPU逻辑个数 : [{}]".format(psutil.cpu_count()))
    print("CPU物理个数 : [{}]".format(psutil.cpu_count(logical=False)))
    # print("CPU所有逻辑信息 : [{}]".format(psutil.cpu_times(percpu=True)))
    print("{}".format("-" * 20))
    '''获取磁盘信息'''
    print("各挂载点及对应的分区: {}".format(psutil.disk_partitions()))
    print("获取根分区'/'信息:{}".format(psutil.disk_usage('/')))  # 'C:\\'
    print("磁盘总的IO个数: {}".format(psutil.disk_io_counters()))
    # print("单个分区io个数、读写信息: {}".format(psutil.disk_io_counters(perdisk=True)))

    # 各挂载分区使用百分比
    disk = [{
        i.mountpoint:
        int(math.ceil(psutil.disk_usage(i.mountpoint).percent))
    } for i in psutil.disk_partitions()]
    for item in disk:
        print(item)
    print("{}".format("-" * 20))
    '''获取网络连接信息'''
    print("总网络IO信息: {}".format(psutil.net_io_counters()))
    print("每个网络接口的IO信息: {}".format(psutil.net_io_counters(pernic=True)))
