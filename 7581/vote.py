#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : vote for the most handsome guy singlepig


def main():
    url = "http://www.qlcoder.com/train/handsomerank?_token=1M0m3KF6DdVNjVLAdE0Z2xUNKHnUeCWNmQOPvfoJ&user=singlepig&checkcode="
    today = datetime.date.today().strftime("%Y%m%d")  # '20160516'
    name = 'singlepig'
    ticket = 1
    checkcode = 0

    while ticket <= 1000:
        m = hashlib.md5()
        m.update((today + name + str(ticket) + str(checkcode)).encode("utf8"))
        if m.hexdigest().startswith("000000"):
            print("checkcode for ticket {} is: {}\nvoting...".format(str(ticket), str(checkcode)))
            req = urlopen(url + str(checkcode))
            print(req.read().decode("utf-8")[0:10])
            ticket += 1
            checkcode = 0
        else:
            checkcode += 1


if __name__ == '__main__':
    import datetime
    import hashlib
    from urllib.request import urlopen

    main()
