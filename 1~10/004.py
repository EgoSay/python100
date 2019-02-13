# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/13 下午8:35
# @IDE     : PyCharm

import calendar


year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

for i in range(1, month):
    """monthlen()函数计算某年份某个月有多少天"""
    day += calendar.monthlen(year, i)

print("it is the %dth day." % day)
