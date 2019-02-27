# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/2/27 下午4:47
# @IDE     : PyCharm

m = dict()
for t1 in ['a', 'b', 'c']:
    if t1 == 'c':
        m.setdefault(t1, 'y')
    elif t1 == 'a':
        m.setdefault(t1, 'z')
    else:
        m.setdefault(t1, 'x')

print("a的对手为:{0},b的对手为:{1},c的对手为:{2}".format(
    m.get('a'), m.get('b'), m.get('c')))
