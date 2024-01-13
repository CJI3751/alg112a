import random

def neighbor(f, p, h):
    dim = len(p)
    p_new = p.copy()
    i = random.randint(0, dim - 1) 
    p_new[i] += random.choice([-h, h]) 
    return p_new, f(*p_new) 

def hillClimbingMin(f, p, h=0.01):
    failCount = 0
    fnow = f(*p)
    while failCount < 10000:
        p1, f1 = neighbor(f, p, h)
        if f1 <= fnow:
            p, fnow = p1, f1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
    return p, fnow

def f(x):
    return x**5 + 1

start_point = [0.0]

min_point, min_value = hillClimbingMin(f, start_point)
print("Minimum point:", min_point)
print("Minimum value:", min_value)
