#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():

    uvUserIdList = []

    with open("./uv.txt", "r") as file:
        for line in file.readlines():
            line = line.strip()
            visitor = line.split(" ")
            uvUserIdList.append(visitor[1])

        print(len(set(uvUserIdList)))


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number = 1))
