# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/26 下午6:27
# @IDE     : PyCharm

height = 100
distance = 0
for i in range(10):
    distance += height + height / 2
    height = height / 2

print("第十次落地时共经过{0}米，第10次反弹高度为{1}米".format(distance - height, height))
