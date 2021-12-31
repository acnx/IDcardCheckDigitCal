#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version 2.7.13 or 3.7.2
# 用于生成身份证号校验位

import random
import re

class IdNumber(str):
    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])
    def get_check_digit(self):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'
if __name__ == '__main__':
    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    a = input("输入前17位：")
    print("校验位为：",IdNumber(a).get_check_digit())  # 校验码:7

