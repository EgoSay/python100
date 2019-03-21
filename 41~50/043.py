# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/21 上午10:04
# @IDE     : PyCharm

class Num:
    # 相当于私有变量
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' %nNum)
        inst.inc()
