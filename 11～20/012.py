# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/21 下午8:52
# @IDE     : PyCharm

for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break

    else:
        print(i)
