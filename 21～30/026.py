# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/9 20:05
# @IDE     : PyCharm


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    print(factorial(5))
