# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/18 下午8:38
# @IDE     : PyCharm
import random

# 生成包含10个随机数的列表
li = random.sample([i for i in range(10000)], 10)
li.sort()
print(li)
