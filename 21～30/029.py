def output(n, li):
    if li == 0:
        return
    print(n[li - 1]),
    output(n, li - 1)


num = input('输入一个正整数 :')
l = len(num)
output(num, l)
print('这是一个%d位数：' % l)
