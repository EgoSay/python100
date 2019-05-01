# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/2 7:07
# @IDE     : PyCharm


data = [i+1 for i in range(20)]
print(data)
i = 1
while len(data) > 1:
    if i % 3 == 0:
        data.pop(0)
    else:
        data.insert(len(data), data.pop(0))
    i += 1
print(data)