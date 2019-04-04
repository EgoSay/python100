# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/2 18:03
# @IDE     : PyCharm
"""
取一个整数a从右端开始的4〜7位(ps: 题目描述不清楚，应该想表达的是二进制取右端开始的4〜7位，如果是十进制取右端开始的4〜7位则不是这种解法)
(1)设置一个4~7位全为1,其余全为0的数: 1111000, 即15 << 3
(2)进行&运算。
"""

a = int(input("请输入一个数:\n"))
print("{}的二进制表示为:{}".format(a, bin(a)))
b = 15 << 3
print("{}的二进制表示为:{}".format(b, bin(b)))
print("二者进行'&'计算后的值为:{},二进制表示为:{}".format((a & b), bin(a & b)))
