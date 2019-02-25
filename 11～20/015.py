# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/25 下午8:10
# @IDE     : PyCharm

score = int(input('输入分数:'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print("{0}分属于评级{1}".format(score, grade))
