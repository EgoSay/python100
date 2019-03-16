# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/16 22:50
# @IDE     : PyCharm
"""
有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。
问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。
问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
"""


def cal_age(age, rank):
    if rank == 1:
        return age
    else:
        return cal_age(age + 2, rank - 1)


print("第五个人年龄为:{}".format(cal_age(10, 5)))
