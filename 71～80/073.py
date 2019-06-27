# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/10 22:13
# @IDE     : PyCharm
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)