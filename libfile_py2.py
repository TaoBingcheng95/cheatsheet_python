# -*- coding: utf-8 -*-
"""
author : Comet
modified time : 2019-9-8
"""

import os
import sys
import platform

try:
    import win32file
except ImportError:
    pass


def mkdir(dirs):
    dirs = dirs.strip()
    dirs = dirs.rstrip("{}".format(os.sep))
    isdir = os.path.isdir(dirs)
    if isdir:
        if_exist = os.path.exists(dirs)
        if not if_exist:
            os.makedirs(dirs)
            print("{} 创建成功".format(dirs))
            return True
        else:
            print("{} 目录已存在".format(dirs))
            return False
    else:
        print("{} 是文件路径".format(dirs))
        return False


def search_dir(dirs, pattern='*', recursive=False, skip_hidden=True, skip_system=True):
    import fnmatch
    dir_list = []
    for file in os.listdir(dirs):
        if fnmatch.fnmatch(file, pattern):
            filepath = os.path.join(dirs, file)
            if os.path.isdir(filepath):
                if recursive:
                    dir_list.extend(search_dir(filepath, recursive=recursive, pattern=pattern))
                else:
                    is_hidden, is_system = file_attribute(item)
                    if skip_hidden and is_hidden:
                        continue
                    if skip_system and is_system:
                        continue
                    dir_list.append(filepath)
    return dir_list


def search_file(dirs, pattern='*', recursive=False, skip_hidden=True, skip_system=True):
    import glob
    import fnmatch
    file_list = []
    path_list = glob.glob(os.path.join(dirs, "*"))
    for item in path_list:
        if os.path.isdir(item):
            if recursive:
                file_list.extend(search_file(item, pattern=pattern, recursive=recursive))
        elif fnmatch.fnmatch(os.path.basename(item), pattern):
            is_hidden, is_system = file_attribute(item)
            if skip_hidden and is_hidden:
                continue
            if skip_system and is_system:
                continue
            file_list.append(item)
    return file_list


def file_attribute(target, is_hidden=False, is_system=False):
    os_name = os.name
    if os_name == 'nt':
        attrs = win32file.GetFileAttributesW(target)
        if attrs & win32file.FILE_ATTRIBUTE_HIDDEN == 2:
            is_hidden = True
        if attrs & win32file.FILE_ATTRIBUTE_SYSTEM == 4:
            is_system = True
    return is_hidden, is_system


def uncompress(srcfile, destdir):
    import gzip
    import tarfile, zipfile
    file = os.path.basename(srcfile)
    if os.path.isfile(file):
        shortname, fmt = os.path.splitext(file)
        fmt = fmt[1:]
        if fmt in ('tgz', 'tar'):
            try:
                tar = tarfile.open(srcfile)
                names = tar.getnames()
                for name in names:
                    tar.extract(name, destdir)
                tar.close()
            except Exception as e:
                print("Can't uncompress {} for {}".format(file, e))
        elif fmt == 'zip':
            try:
                zipfile = zipfile.ZipFile(srcfile)
                for names in zipfile.namelist():
                    zipfile.extract(names, destdir)
                zipfile.close()
            except Exception as e:
                print("Can't uncompress {} for {}".format(file, e))
        elif fmt == 'gz':
            try:
                fname = os.path.join(destdir, os.path.basename(srcfile))
                gfile = gzip.GzipFile(srcfile)
                open(fname, "w+").write(gfile.read())
                # gzip对象用read()打开后，写入open()建立的文件中。  
                gfile.close()
                # 关闭gzip对象  
            except Exception as e:
                return False, e, fmt
        '''
        elif fmt == 'rar':
            try:
                rar = rarfile.RarFile(srcfile)  
                os.chdir(destdir)
                rar.extractall()  
                rar.close()  
            except Exception as e :
                return (False, e, filefmt)
        '''
    else:
        print('文件格式不支持或者不是压缩文件')
    return None


if __name__ == '__main__':

    source_root = os.getcwd()
    tmp = search_file(source_root, recursive=False, skip_hidden=True)
    for item in tmp:
        print(item)

    # print(sys.platform)
    # print("操作系统类型 : [{}]".format(platform.system()))
    # print(os.name)
