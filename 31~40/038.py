# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/18 下午8:38
# @IDE     : PyCharm
from _operator import add
from functools import reduce

import numpy as np


# 随机生成矩阵
def create_matrix(row, column):
    return np.random.randint(0, 1000, size=[row, column])


# 计算矩阵对角线之和
def cal_matrix_diagonal(matrix):
    # trace()方法直接可以求'\'对角线之和
    print(matrix.trace())

    # 分别计算('/'和'\'对角线之和)
    left_diag = reduce(add, matrix.diagonal())
    right_diag = reduce(add, matrix[::-1].diagonal())

    return left_diag + right_diag - matrix[2, 2]


# TODO 扩展成求任意矩阵对角线之和
def cal_matrix_diagonal_all():
    """

    :return:
    """


if __name__ == '__main__':
    matrix = create_matrix(3, 3)
    print("生成的矩阵为:\n{}".format(matrix))
    print("\n==========================\n")
    print("矩阵对角线上的数和为:{}".format(cal_matrix_diagonal(matrix)))
