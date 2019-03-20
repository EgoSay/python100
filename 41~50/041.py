# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/20 上午9:54
# @IDE     : PyCharm


class StaticVar():
    __count = 0  # 私有变量，无法在外部访问，Foo.__count会出错

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls, num):
        cls.__count = num

    @classmethod
    def varfunc(cls):
        cls.__count += 1
        print(cls.__count)


f1 = StaticVar()
f2 = StaticVar()
StaticVar.set_count(1)
for i in range(3):
    f1.varfunc()

for i in range(3):
    f2.varfunc()
