# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/18 11:22
# @IDE     : PyCharm
if __name__ == '__main__':
    ls = []
    str1 = input("string1:\n")
    str2 = input("string2:\n")
    str3 = input("string3:\n")
    ls.extend([str1, str2, str3])
    ls.sort()
    print(ls)
