# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/2 17:58
# @IDE     : PyCharm
"""
0^0=0; 0^1=1; 1^0=1; 1^1=0
1010 ^ 0101  ==>  1111
"""
a = 10    # 二进制 1010
b = a ^ 5  # 3的二进制 0101
print('a | b = %d' % b)
b ^= 7
print('a | b = %d' % b)