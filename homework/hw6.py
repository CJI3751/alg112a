def gradient_descent(f, start_point, learning_rate=0.01, max_iterations=1000, tolerance=1e-6, step=1e-4):
    p = start_point.copy()
    for iteration in range(max_iterations):
        gradient = grad(f, p, step)
        new_p = [p[i] - learning_rate * gradient[i] for i in range(len(p))]

        if sum((new_p[i] - p[i])**2 for i in range(len(p))) < tolerance**2:
            break

        p = new_p

    return p, f(p)

def df(f, p, k, step):
    p1 = p.copy()
    p1[k] += step
    return (f(p1) - f(p)) / step


def grad(f, p, step):
    return [df(f, p, k, step) for k in range(len(p))]


def example_function(p):
    return sum(x**2 for x in p)

start_point = [5, 5]
min_point, min_value = gradient_descent(example_function, start_point)
print("Minimum point:", min_point)
print("Minimum value:", min_value)
