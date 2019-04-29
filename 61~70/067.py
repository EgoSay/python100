# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/29 10:14
# @IDE     : PyCharm
import random


def swap(arr):
    max_index = 0
    min_index = len(arr) - 1
    for i in range(0, len(arr)):
        if arr[max_index] < arr[i]:
            max_index = i
        if arr[min_index] > arr[1]:
            min_index = i
    print("最大值为:{},最小值为:{}\n".format(arr[max_index], arr[min_index]))
    arr[max_index], arr[0] = arr[0], arr[max_index]
    arr[min_index], arr[len(arr) - 1] = arr[len(arr) - 1], arr[min_index]
    return arr


if __name__ == '__main__':
    arr = [random.randrange(3, 100, 2) for i in range(10)]
    print("随机生成的数组:{}\n".format(arr))
    print("计算处理后的数组:{}".format(swap(arr)))