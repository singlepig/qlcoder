#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : 千里码 - 码之初


def main():
    n = 0
    num = 0
    while n < 2333:
        num += 1
        if (num % 2 == 0 or num % 3 == 0):
            n += 1

    print("the 2333 number is: {}".format(num))


if __name__ == '__main__':
    main()
