# @Author  : adairchan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/5/18 11:13
# @IDE     : PyCharm
import operator

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
max_age = max(person.items(), key=operator.itemgetter(1))[0]
print("年龄最大的为:{},其年龄为{}岁".format(max_age, person.get( max_age)))
