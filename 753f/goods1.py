#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : 商品数量1


def main():
    file_name = "144043123647536.txt"
    with open(file_name, mode='r') as f:
        lines = f.readlines()
        goods = {}
        query_sum = 0
        for line in lines:
            line = line.strip()
            (opt, num, price) = line.split(" ")
            if opt == "query":
                down_limit, up_limit = num, price
                if down_limit not in goods:
                    goods[down_limit] = 0  # 添加下限
                if up_limit not in goods:
                    goods[up_limit] = 0  # 添加上限
                goods_price = sorted(goods, key=lambda x: int(x))
                for x in range(goods_price.index(down_limit), goods_price.index(up_limit) + 1):
                    query_sum += goods[goods_price[x]]

            if opt == "up":
                if price in goods:
                    goods[price] += int(num)  # 已经有该价格的衣服，修改数量
                else:
                    goods[price] = int(num)  # 没有该价格的衣服，加入记录

            if opt == "down":
                goods[price] -= int(num)  # 下架操作，更改数量

        print("query sum is: " + str(query_sum))

if __name__ == '__main__':
    main()
