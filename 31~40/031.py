# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/3/17 下午5:28
# @IDE     : PyCharm


week_list = {'M': 'Monday', 'T': {'u': 'Tuesday', 'h': 'Thursday'}, 'W': 'Wednesday', 'F': 'Friday',
             'S': {'a': 'Saturday', 'u': 'Sunday'}}
sLetter1 = input("请输入首字母：")
sLetter1 = sLetter1.upper()

if sLetter1 in ['T', 'S']:
    sLetter2 = input("请输入第二个字母：")
    print(week_list[sLetter1][sLetter2])
else:
    print(week_list[sLetter1])
