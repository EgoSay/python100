# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/15 下午4:54
# @IDE     : PyCharm
import time

for i in range(1, 5):
    time.sleep(1)
    print("第{}次输出，当前时间为:{}".format(i, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
