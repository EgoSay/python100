# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/25 下午8:33
# @IDE     : PyCharm


space = digit = letter = others = 0
string = str(input("输入一串字符:"))
for s in string:
    if s.isspace():
        space += 1
    elif s.isalpha():
        letter += 1
    elif s.isdigit():
        digit += 1
    else:
        others += 1

print("这串字符中字母共有{0}个，数字共有{1}个，空格共有{2}个，其他字符{3}个".format(letter, digit, space, others))
