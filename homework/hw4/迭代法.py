from numpy import arange
f1 = lambda x: (x*x + 1) / 3
f2 = lambda x: 3 - (1/x)
f3 = lambda x: (x-3)*(x+1) + 4

x1 = x2 = x3 = 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2:', x2, 'x3:', x3)
