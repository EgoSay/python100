# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/1/23 下午5:00
# @IDE     : PyCharm

profit = int(input("请输入今年的公司利润："))
percent = {1000000: 0.01, 600000: 0.015, 400000: 0.03, 200000: 0.05, 100000: 0.075, 0: 0.1}
keys = percent.keys()
keys = sorted(keys, reverse=True)

bonus = 0
for key in keys:
    if profit > key:
        bonus += (profit - key) * percent.get(key)
        profit = key
print("发放奖金总数为:{0}元".format(bonus))

