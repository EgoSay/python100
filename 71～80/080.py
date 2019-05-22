# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/18 11:22
# @IDE     : PyCharm

if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while i < 5:
        x = 4 * j
        for i in range(0, 5):
            if x % 4 != 0:
                break
            else:
                i += 1
            x = (x / 4) * 5 + 1
        j += 1
    print(x)
