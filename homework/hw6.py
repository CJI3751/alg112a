import random

def neighbor(f, p, h):
    dim = len(p)
    p_new = p.copy()
    i = random.randint(0, dim - 1)  # 随机选择一个维度
    p_new[i] += random.choice([-h, h])  # 在该维度上增加或减少一个小的步长
    return p_new, f(*p_new)  # 返回新的点和该点的函数值

def hillClimbing(f, p, h=0.01):
    failCount = 0
    fnow = f(*p)
    while failCount < 10000:
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            p, fnow = p1, f1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
    return p, fnow

def f(x, y, z):
    return -1 * (x**2 + y**2 + z**2)

best_p, best_f = hillClimbing(f, [2, 1, 3])
print("Best point:", best_p)
print("Best value:", best_f)
