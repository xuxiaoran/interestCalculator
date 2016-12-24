#!/usr/in/python
# -*- coding: utf-8 -*-

import math

keep_going = True

while keep_going:
	principle = int(input("本金(万): ")) * (10**4)
	interest = float(input("输入利率: ") * 0.01)/365.0000
	time = int(input("天数: "))
	print "收益: %0.02f" % (principle * interest * time)

	command = raw_input("计算下一个按c，否则退出")
	print command
	if not command == "c":
		keep_going = False
