#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : 老王装货


def main():
    goods = [509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]
    load_capacity = 5000  # 总载重
    load_list = []  # 货物列表
    # sum(load_list) 列表载重量

    for i in range(0, len(goods)):
        rets = list(itertools.combinations(goods, i))
        for ret in rets:
            s = sum(ret)
            if s <= load_capacity and s > sum(load_list):
                load_list = ret

    a = "-".join([str(goods.index(i) + 1) for i in load_list])
    print("最大载重：{}\n载货重量分别为：{}\n序号为：{}".format(sum(load_list), str(load_list), a))

if __name__ == '__main__':
    import itertools
    main()
