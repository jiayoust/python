import math


def Distance(x, y, p=2):
    if len(x) == len(y) and len(x) > 1:
        sum = 0
        for i in range(len(x)):  # len()长度
            sum += math.pow(abs(x[i] - y[i]), p)  # abs()绝对值
        return math.pow(sum, 1 / p)  # math.pow(x,y)x的y次方
    else:
        return 0


x1 = [1, 1]
x2 = [5, 1]
x3 = [4, 4]

for i in range(1, 5):
    # format格式化函数{}相当于%
    r = {'{}-{}'.format(i, c): Distance(x1, c, p=i) for c in [x2, x3]}
    print(min(zip(r.values(), r.keys())))
