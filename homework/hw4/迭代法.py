def f(x):
    return x**2 - 3*x + 1

def df(x):
    return 2*x - 3
f1 = lambda x: x - f(x)/df(x)
f2 = lambda x: (x**2 + 1) / 3
f3 = lambda x: (3*x - 1)**0.5

x1 = x2 = x3 = 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2:', x2, 'x3:', x3)
