#!/usr/bin/env python3

"""setup pyton develop environment


"""

import os
import sys

HOME = os.environ.get("HOME", "HOME DO NOT EXSIT")


def main(argc, argv):
    global HOME
    if __debug__:
        print("[Debug]: use HOME be {}/tmp/test/".format(HOME))
        HOME = HOME + "/tmp/test"

    # config the pipy mirror:
    print("Setting pipy mirror...  ", end='')
    os.system("mkdir -p {}/.pip".format(HOME))

    try:
        pip_conf_fp = open('{}/.pip/pip.conf'.format(HOME), 'w')
        pip_conf_fp.write(
            "[global]\n"
            "index-url = https://pypi.tuna.tsinghua.edu.cn/simple\n")
        print("OK")
    except IOError as e:
        print("should not be error, but what's wrong?", file=sys.stderr)
        print("IOError: ", e, file=sys.stderr)
    finally:
        if 'pip_conf_fp' in locals():
            pip_conf_fp.close()

    # === install basic packages ===
    print("upgrade pip in USER local...", "\n{}".format('=' * 20))
    os.system("pip3 install --user --upgrade pip")
    print(('=' * 20), '\nupgrade pip in USER local... OK')

    print("\ninstall >>>>ipython<<< in USER local...", "\n{}".format('=' * 20))
    os.system("pip3 install --user ipython")
    print(('=' * 20), "\ninstall ipython in USER local...  OK")

    print("\ninstall >>>>virtualenv & virtualenvwrapper<<<< in USER local...",
          '\n{}'.format('=' * 20))
    os.system("pip3 install --user virtualenv")
    print(('=' * 20), '\ninstall virtualenv & virtualenvwrapper in USER local...  OK')

    # print("\nsetup virtualenvwrapper in ~/.bashrc...")


if __name__ == '__main__':
    # check running user(root? normal?)
    # ...code...

    # check python version
    # ...should be python3

    main(len(sys.argv), sys.argv)
