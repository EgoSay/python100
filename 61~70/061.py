# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/23 22:38
# @IDE     : PyCharm


def Pascal(n):
    ls = [[1]]
    for i in range (1, n):
        ls.append([1])
        for j in range(1, i):
            ls[i].append(ls[i-1][j-1] + ls[i-1][j])
        ls[i].append(1)
    for i in range(0, n):
        print(ls[i])
    return ls


a = Pascal(10)