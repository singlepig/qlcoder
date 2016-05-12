#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : guess shinian's password


def main():
    pass_md5 = "7E38890B870934B126F66857ED6B57B9"
    startDate = 20000000
    # TODO
    # 暴力破解不科学，应该把日期变成按日为单位变化
    while not checkmd5(str(startDate).encode("utf8"), pass_md5.lower()):
        startDate -= 1
        print(startDate)

def checkmd5(str, md5str):
    m = hashlib.md5()
    m.update(str)
    if m.hexdigest() == md5str:
        print("shinian's password is : {}".format(str))
        return True
    return False

if __name__ == '__main__':
    import  hashlib
    main()
