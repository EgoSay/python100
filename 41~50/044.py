# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     : PyCharm
import numpy as np

def create_matrix(row, column):
    return np.random.randint(0, 100, size=[row, column])


def matrix_add(matrix1, matrix2):
    return matrix1 + matrix2


if __name__ == '__main__':
    matrix1 = create_matrix(3, 3)
    print("矩阵1:\n{}\n".format(matrix1))
    matrix2 = create_matrix(3, 3)
    print("矩阵2:\n{}\n".format(matrix2))
    print(matrix_add(matrix1, matrix2))
