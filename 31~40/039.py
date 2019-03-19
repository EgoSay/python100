# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/18 下午8:38
# @IDE     : PyCharm


a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
b = 18

# 对半查找,提高效率
f0, f1 = 0, len(a) - 1
while f1 - f0 > 1:
    mid = f0 + int((f1 - f0) / 2)
    if a[mid] > b:
        f1 = mid
    else:
        f0 = mid
a.insert(f0 + 1, b)
print(a)
