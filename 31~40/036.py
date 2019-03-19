# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/18 下午8:24
# @IDE     : PyCharm


for i in range(1, 101):
    for j in range(2, i // 2):
        if i % j == 0:
            break
    else:
        print(i)
