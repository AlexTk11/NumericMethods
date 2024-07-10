from Solvers import Six_Point, Implicit_NonLinear, Implicit_Linear
from Tasks import tasks
import matplotlib.pyplot as plt
import numpy as np

set_t = 2 #момент времени для вывода графика

cur_task = tasks[1]

accuracy = 0.1
s = Six_Point(cur_task, interval = cur_task.l , eps = accuracy)

while (s.time < set_t):
    s.precision_step()
    
plt.plot(s.linspace, s.solution)

true_res = []
for i in s.linspace:
    true_res.append(cur_task.solution(i, s.time))
plt.plot(s.linspace, true_res)
plt.show()