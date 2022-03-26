# 计算机202 马湘明

import numpy.random

# 圆周率
# 统计数量级为nc
c = 10
n = 10000000
r = 1.0
# 圆心
a, b = (0., 0.)
# 边界
x_min, y_min, x_max, y_max = a - r, b - r, b + r, a + r
# 定积分
x_min1, x_max1 = 0.0, 1.0
y_min1, y_max1 = 0.0, 1.0
# 极值
x_min2, x_max2 = -2.0, 2.0
k = 200
f = lambda x: k * (numpy.sin(x) * numpy.exp(-0.05 * x))


def GetPi():
    x = numpy.random.uniform(x_min, x_max, n)
    y = numpy.random.uniform(y_min, y_max, n)
    l = numpy.sqrt(pow((x - a), 2) + pow((y - b), 2))
    count = sum(numpy.where(l < r, 1, 0))
    pi = 4 * count / n
    return pi


def GetDefiniteIntegral():
    x = numpy.random.uniform(x_min1, x_max1, n)
    y = numpy.random.uniform(y_min1, y_max1, n)
    count = sum(numpy.where(y < pow(x, 2), 1, 0))
    ans = count / n
    return ans


def GetMaxAndMinVal():
    # x = numpy.random.uniform(x_min2, x_max2, n)
    # return [k * numpy.max(numpy.sin(x) * numpy.exp(-0.05 * x))]
    list = [0.0, 0.0]
    for i in range(0, n):
        x = numpy.random.uniform(x_min2, x_max2)
        F = f(x)
        if F > list[0]:
            list[0] = F
            list[1] = x
    return list


if __name__ == '__main__':
    P = 0
    for i in range(0, c):
        p = GetPi()
        print(p)
        P += p
    print(P / c)
    ans = 0
    for i in range(0, c):
        ans += GetDefiniteIntegral()
    print(ans/c)
    print(GetMaxAndMinVal())
