# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/1/23 下午4:22
# @IDE     : PyCharm

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (i != k) and (j != k):
                print(i*100 + j*10 + k)

