#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author        : singlepig
# Email         : gys.nanjing@gmail.com
# Description   : 千里基注册推荐


import string
import random
import datetime


def gen_username():
    username_length = random.randint(3, 7)
    username = ''.join(random.sample(string.ascii_letters, username_length))
    if username in gays:
        print("name {name} is registered".format(name=username), file=logs)
        return gen_username()
    else:
        gays.append(username)
    return username


def gen_password():
    password_length = random.randint(20, 30)
    password = ''.join(random.sample(string.ascii_letters + string.digits, password_length))
    return password


def gen_birthday():
    '''随机生成日期，姿势不太好'''
    year = random.randint(1970, 2015)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birthday = datetime.datetime(year, month, day)
    return birthday.strftime("%Y%m%d")  # "19700101"


def generate_gays():
    username = gen_username()
    password = gen_password()
    email = username + "@qlcoder.com"
    sex = random.randint(0, 1)
    birthday = gen_birthday()
    introducer = "singlepig"
    phone = '1' + ''.join(random.sample(string.digits, 10))

    gay = {
        "username": username,
        "password": password,
        "re-password": password,
        "birthday": birthday,
        "email": email,
        "sex": sex,
        "phone": phone,
        "introducer": introducer
    }

    print("new gay: {}".format(gay), file=logs)
    return gay


def main():
    for x in range(0, 1000):
        generate_gays()


if __name__ == '__main__':
    gays = []
    logs = open("log.txt", mode='w')
    main()
    logs.close()
