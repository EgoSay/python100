# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/14 下午3:34
# @IDE     : PyCharm

x = int(input('输入x:\n'))
y = int(input('输入y:\n'))
z = int(input('输入z:\n'))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y

print((x, y, z))
