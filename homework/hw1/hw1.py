#參考自ChatGPT
from datetime import datetime

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 可以将 n 设定为 10，40 或 60
n = 60
startTime = datetime.now()
print(f'fibonacci_iterative({n})={fibonacci_iterative(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time: {seconds}')
