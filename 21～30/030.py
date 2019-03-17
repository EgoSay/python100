# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/17 下午5:05
# @IDE     : PyCharm


def palindrome(n, flag=True):
    for i in range(len(n)):
        if n[i] != n[len(n) - 1 - i]:
            flag = False
            break
    return flag


if __name__ == '__main__':
    n = input()
    flag = palindrome(n)
    if flag:
        print("{}是一个回文数".format(n))
    else:
        print("{}不是一个回文数".format(n))
