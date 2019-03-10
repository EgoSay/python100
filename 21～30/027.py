# @Author  : codeAC
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/10 21:18
# @IDE     : PyCharm


def output(s, index):
    if index == 0:
        return
    else:
        print(s[index - 1])
        output(s, index - 1)


if __name__ == '__main__':
    s = 'dcfkvl'
    output(s, len(s))
