# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/1/24 下午4:45
# @IDE     : PyCharm

"""
设该数为x：x + 100 = n^2, n^2 + 168 = m^2。

设m=n+k（不妨设m,n,k均为自然数）：代入m^2-n^2-168，得k^2+2nk=168。

解得n=84/k - k/2；由于n,k均为自然数，则nk>=1，故1<=k^2<168，故1<=k<=12
"""

for i in range(1, 13):
    a = 84/i - i/2
    # if type(a) == int:
    if int(a) == a:
        print(a**2 - 100)
