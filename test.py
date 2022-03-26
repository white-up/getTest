import matplotlib.pyplot as plt
import numpy as np

b_xs = []
b_ys = []


# xs表示原始数据
# n表示阶数
# k表示索引
def one_bezier_curve(a, b, t):
    return (1 - t) * a + t * b


def n_bezier_curve(xs, n, k, t):
    if n == 1:
        return one_bezier_curve(xs[k], xs[k + 1], t)
    else:
        return (1 - t) * n_bezier_curve(xs, n - 1, k, t) + t * n_bezier_curve(xs, n - 1, k + 1, t)


def bezier_curve(xs, ys, num, b_xs, b_ys):
    n = 3  # 采用3次bezier曲线拟合
    t_step = 1.0 / (num - 1)
    # t_step = 1.0 / num
    # print(t_step)
    t = np.arange(0.0, 1 + t_step, t_step)
    # print(len(t))
    for each in t:
        b_xs.append(n_bezier_curve(xs, n, 0, each))
        b_ys.append(n_bezier_curve(ys, n, 0, each))


def func():
    # xs = [1.0, 2.1, 3.0, 4.0, 5.0, 6.0]
    xs = [237, 237, 143, 143, 435, 435, 339, 339, 552, 576, 570, 6, 0, 24, 183]
    # ys = [0, 1.1, 2.1, 1.0, 0.2, 0]
    ys = [620, 120, 19, 0, 0, 19, 109, 620, 492, 492, 662, 662, 492, 492, 620]
    num = 5
    Xs = [
        [237, 237, 237, 237],
        [237, 237, 226, 143],
        [143, 143, 143, 143],
        [143, 143, 435, 435],
        [435, 435, 435, 435],
        [435, 353, 339, 339],
        [339, 339, 339, 339],
        [339, 507, 529, 552],
        [552, 552, 576, 576],
        [576, 576, 570, 570],
        [570, 570, 6, 6],
        [6, 6, 0, 0],
        [0, 0, 24, 24],
        [24, 48, 71, 183],
        [183, 183, 237, 237]
    ]
    Ys = [
        [620, 620, 120, 120],
        [120, 35, 24, 19],
        [19, 19, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 19, 19],
        [19, 23, 36, 109],
        [109, 108, 620, 620],
        [620, 620, 602, 492],
        [492, 492, 492, 492],
        [492, 492, 662, 662],
        [662, 662, 662, 662],
        [662, 662, 492, 492],
        [492, 492, 492, 492],
        [492, 492, 620, 620],
        [620, 620, 620, 620]
    ]

    bezier_curve(xs, ys, num, b_xs, b_ys)  # 将计算结果加入到列表中
    print(b_xs, b_ys)
    plt.figure()
    # plt.plot(b_xs, b_ys, 'r')  # bezier曲线
    for i in range(15):
        ax = []
        ay = []
        bezier_curve(Xs[i], Ys[i], num, ax, ay)
        plt.plot(ax, ay, 'r')
    for i in range(15):
        plt.plot(Xs[i], Ys[i])
    # plt.plot(xs, ys)  # 原曲线
    plt.show()


func()
