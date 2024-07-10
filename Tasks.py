import numpy as np

class Task:
    def __init__(self, l, f, alpha, mu1, mu2, solution=None, k=None):
        self.l = l
        self.k = k
        self.f = f
        self.alpha = alpha
        self.mu1 = mu1
        self.mu2 = mu2
        self.solution = solution

task0 = Task(
    l=1,
    f=lambda x, t: np.sin(x),
    alpha=lambda x: np.cos(x) + np.sin(x),
    mu1=lambda t: np.exp(-t),
    mu2=lambda t: np.exp(-t) * np.cos(1) + np.sin(1),
    solution=lambda x, t: np.exp(-t) * np.cos(x) + np.sin(x)
)

task1 = Task(
    l=1,
    f=lambda x, t: 2 * np.exp(t) * np.cos(x),
    alpha=lambda x: np.cos(x),
    mu1=lambda t: np.exp(t),
    mu2=lambda t: np.exp(t) * np.cos(1),
    solution=lambda x, t: np.exp(t) * np.cos(x)
)

task2 = Task(
    l=1,
    k=lambda u: 0.001 * u,
    f=lambda u: 0.003 * np.power(u, 4),
    alpha=lambda x: 5 * np.sin(np.pi * x),
    mu1=lambda t: 0,
    mu2=lambda t: 0
)

task3 = Task(
    l=1,
    k=lambda u: 0.007 * np.power(u, 2),
    f=lambda u: 0.003 * u,
    alpha=lambda x: -5 * (x - 0.2) * (x - 0.8),
    mu1=lambda t: 0,
    mu2=lambda t: 0
)

task4 = Task(
    l=1,
    k=lambda u: 0.007 * np.power(u, 2),
    f=lambda u: 0.003 * u,
    alpha=lambda x: np.abs(5.65 * np.sin(2 * np.pi * x)),
    mu1=lambda t: 0,
    mu2=lambda t: 0
)

tasks = [task0, task1, task2, task3, task4]