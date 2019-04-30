# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/30 20:30
# @IDE     : PyCharm
"""
优化解法，先将前m个数逆转，再将后面的数逆转，最后全部逆转，相当于就是把这前m个数后移了
"""
import random


def swap(arr, start, end):
    """
    :param arr: 整数列表
    :param start: 逆转列表的头
    :param end:  逆转列表的尾
    :return: 逆转完成后的数组
    """
    i, j = start, end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


if __name__ == '__main__':
    n = int(input("请m输入整数个数:"))
    m = int(input("请输入需要移动的位置:"))
    # 随机生成数组
    arr = [random.randrange(3, 100, 2) for i in range(n)]
    m = len(arr) - m
    print(arr)
    arr = swap(arr, 0, m - 1)
    print(arr)
    arr = swap(arr, m, len(arr) - 1)
    print(arr)
    print(swap(arr, 0, len(arr) - 1))
