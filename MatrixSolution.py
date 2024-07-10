
import math
import numpy as np

def solve_matrix(n, a, b, c, f) -> list:
    """Solves a - c + b = -f"""
    alpha = [0.] * (n + 2)
    beta = [0.] * (n + 2)
    y = [0.] * (n + 1)

    alpha[1] = b[0] / c[0]
    beta[1] = f[0] / c[0]

    for i in range(1, n):
        alpha[i + 1] = b[i] / (c[i] - alpha[i] * a[i])
        beta[i + 1] = (a[i] * beta[i] + f[i]) / (c[i] - alpha[i] * a[i])

    beta[n + 1] = (a[n] * beta[n] + f[n]) / (c[n] - alpha[n] * a[n])
    y[n] = beta[n + 1]

    for i in range(n - 1, -1, -1):
        y[i] = alpha[i + 1] * y[i + 1] + beta[i + 1]

    return y


def set_acc(eps):
    l = 1
    t = eps
    h = math.sqrt(2 * t)
    n = math.floor(l / h)
    h = l / n
    xs = np.linspace(0, l, n)
    return 101, 0.01
    # return n + 1, t

