# @Author  : adair_chan
# @Email   : adairchan.dream@gmail.com
# @Date    : 2019/4/13 上午10:10
# @IDE     : PyCharm

import matplotlib.pyplot as plt
import numpy as np

x = y = np.arange(-11, 11, 0.1)
x, y = np.meshgrid(x, y)
# 圆心为（0，0），半径为1-10
for i in range(1, 11):
    plt.contour(x, y, x ** 2 + y ** 2, [i ** 2])
    # 如果删除下句，得出的图形为椭圆
    plt.axis('scaled')
plt.show()
