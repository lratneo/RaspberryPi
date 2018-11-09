#!/usr/bin/env python3

""" auto setup RaspberryPi Ubuntu MATE system apt source mirror

Usage:
    $ sudo python -O /path/to/this/file/dir/ubuntu-mate.py

"""

import sys
import os

HOME = os.environ.get("HOME", 'HOME NOT EXSIT')

MIRROR_URL = "http://mirrors.ustc.edu.cn/ubuntu-ports/"

ORIGINAL_URL = "http://ports.ubuntu.com/"


def main(argc, argv):
    print(HOME)

    # os.system("cp /etc/apt/sources.list {}/backup/root/etc/apt/sources.list".format(HOME))

    mirror_sources_list_filestr = ""
    try:
        if __debug__:
            fp = open("{}/backup/root/etc/apt/sources.list".format(HOME))
            print("original sources.list:\n", fp.read())
            fp.seek(0)
        else:
            fp = open("/etc/apt/sources.list", 'r')
        for line in fp:
            mirror_sources_list_filestr += line.replace(ORIGINAL_URL, MIRROR_URL)
        if __debug__:
            print("change to CN mirror:\n", mirror_sources_list_filestr)
    except:
        print("permission issue?", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'fp' in locals():
            fp.close()

    try:
        fp = open('/etc/apt/sources.list', 'w')
        fp.write(mirror_sources_list_filestr)
    except:
        print("permission issue?", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'fp' in locals():
            fp.close()


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
