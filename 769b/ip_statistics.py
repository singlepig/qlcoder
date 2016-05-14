#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : 统计ip归属地为北京、杭州、深圳、上海的ip数量


def main():
    f = open("./taobaoip/ip.data", "r", encoding="ISO-8859-1")
    data = f.read()
    f.close()

    result = {}

    for i in range(0, len(data), 5):
        # t = (ord(data[i + 2]) << 8) + ord(data[i + 3])
        t = ord(data[i + 2]) * 256 + ord(data[i + 3])
        if t in result:
            result[t] += 256
        else:
            result[t] = 256

    print("杭州：" + str(result[242]))
    print("北京：" + str(result[29]))
    print("上海：" + str(result[133]))
    print("深圳：" + str(result[75]))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number=1))
