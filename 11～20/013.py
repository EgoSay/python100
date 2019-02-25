# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/25 下午3:46
# @IDE     : PyCharm

# hundred ,ten_digits, digits= 0

for i in range(100, 1000):
    hundred = int(i / 100)
    ten_digits = int(i % 100 / 10)
    digits = int(i % 10)
    if i == hundred ** 3 + ten_digits ** 3 + digits ** 3:
        print(i)
