# -*- coding: utf-8 -*-
import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

# 设置字体
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 定义数据
N = 300
Xlim = 100  # 允许移动的最大范围
np.random.seed(N)

X1 = Xlim * np.random.rand(N)  # 生成N个[0, 1)的浮点数
X2 = Xlim * np.random.rand(N)  # X1 + X1**2 - 5

persons_ar = np.ndarray((1, N, 3))
persons_ar[0, :, 0] = X1
persons_ar[0, :, 1] = X2
persons_ar[0, :, 2] = 0
# 让坐标在 [0, Xlim]范围内
persons_ar[0, :, 0][persons_ar[0, :, 0] < 0] = 0
persons_ar[0, :, 0][persons_ar[0, :, 0] > Xlim] = Xlim
persons_ar[0, :, 1][persons_ar[0, :, 1] < 0] = 0
persons_ar[0, :, 1][persons_ar[0, :, 1] > Xlim] = Xlim

persons_ar[0, 0, 2] = 1  # 把(0,0)位置的status改为1

# print('==persons_ar==')
# print(persons_ar)
# print('====================')
# print(persons_ar[0, :, 0])  # 显示X
# print('====================')

delta_X1 = np.random.randint(low=-1, high=2, size=N) * \
    np.random.rand(N)/5.0  # N个随机的横轴该变量
# print(delta_X1)
print('====================')
persons_ar[:, :, 0] = persons_ar[:, :, 0] + delta_X1
#print(persons_ar[0, :, 0])

# endregion

# region 绘制动画
# 确定画布

plt.figure(figsize=(12, 8), dpi=100)
plt.ion()
for itors in range(50000):
    # 清空旧的画布
    plt.cla()
    plt.xlim((-1, Xlim*1.2))
    plt.ylim((-1, Xlim*1.2))

    delta_X1 = np.random.randint(
        low=-1, high=2, size=N)*np.random.rand(N)  # N个随机的横轴该变量
    delta_X2 = np.random.randint(low=-1, high=2, size=N)*np.random.rand(N)
    persons_ar[0, :, 0] = persons_ar[0, :, 0] + delta_X1
    persons_ar[0, :, 1] = persons_ar[0, :, 1] + delta_X2
    # 让坐标在 [0, Xlim]范围内
    persons_ar[0, :, 0][persons_ar[0, :, 0] < 0] = 0
    persons_ar[0, :, 0][persons_ar[0, :, 0] > Xlim] = Xlim
    persons_ar[0, :, 1][persons_ar[0, :, 1] < 0] = 0
    persons_ar[0, :, 1][persons_ar[0, :, 1] > Xlim] = Xlim

    Statuses = np.unique(persons_ar[0, :, 2])  # 取所有的状态
    for status in Statuses:
        persons_in_status = persons_ar[persons_ar[:, :, 2] == status]
        if status == 1:
            color = 'red'
        else:
            color = 'blue'
        plt.scatter(persons_in_status[:, 0], persons_in_status[:, 1],  # 散点的横、纵坐标序列
                    s=30,   # 点
                    c=color,
                    label="Label Positive")
    plt.legend()  # 显示图例说明
    plt.pause(0.001)
# endregion 绘制动画
