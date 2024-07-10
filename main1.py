from Solvers import Six_Point, Implicit_NonLinear, Implicit_Linear
from Tasks import tasks
import matplotlib.pyplot as plt
import numpy as np

set_t = 0.1 #момент времени для вывода графика

cur_task = tasks[2] #номер решаемой задачи (tasks.py)

accuracy = 0.01
#res = SixPointSolver(cur_task, interval = cur_task.l , eps = accuracy)
s = Implicit_Linear(cur_task, interval = cur_task.l , eps = accuracy)
while (s.time < set_t):
    sol = s.next()
    s.time += s.dt
    s.solution = sol


plt.plot(s.linspace, s.solution)

plt.show()



