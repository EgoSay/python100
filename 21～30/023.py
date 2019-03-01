# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/1 下午5:26
# @IDE     : PyCharm

for i in range(1, 5):
    print(' ' * (4 - i), end="")
    for j in range(1, 2 * i):
        print('*', end="")
    print()
for i in range(3, 0, -1):
    print(' ' * (4 - i), end="")
    for j in range(1, 2 * i):
        print('*', end="")
    print()
