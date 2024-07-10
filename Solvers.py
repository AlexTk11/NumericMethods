import numpy as np
from MatrixSolution import solve_matrix, set_acc


class BaseSolver:
    def __init__(self, task, interval, eps):
        self.task = task
        self.interval = interval
        self.eps = eps

        #print(self.interval)
        self.point_count, tau = set_acc(eps)
        self.steps = (self.interval / (self.point_count - 1), tau)  # h, tau
        self.linspace = (np.linspace(0, self.interval, self.point_count))

        self.solution = self.task.alpha(self.linspace)
        self.dx, self.dt = self.steps
        self.dt = self.dx ** 2
        #print(self.point_count)
        #print(self.dx, self.dt)
        self.time = 0
        #print(self.linspace)

    def next(self):
        pass

    def precision_step(self):
        dt_solution, half_dt_solution = np.ones_like(self.linspace), np.zeros_like(self.linspace)
        while np.linalg.norm(dt_solution - half_dt_solution) >= self.eps:
            # step with dt
            dt_solution = self.next()

            # 2 steps with 0.5 * dt
            self.dt /= 2

            solution = self.solution  # temporarily save old data
            t = self.time

            self.solution = self.next()  # proceed with half-step
            self.time += self.dt  # adjust data

            half_dt_solution = self.next()

            self.solution = solution  # return data
            self.time = t

            # print(np.all(dt_solution == half_dt_solution))

            print(self.time, self.dt)

        # print(self.time)
        self.dt *= 2
        self.time += self.dt

        print(self.dt)

        self.solution = self.next()

        return self.solution


class Six_Point(BaseSolver): #Схема с весами

    def __init__(self, task, interval, eps):
        super().__init__(task, interval, eps)
        
        self.sigma = 0.5

    def next(self):
        gamma = self.dt / self.dx ** 2

        a = [0]
        c = [1]
        b = [0]
        f = [self.task.mu1(self.time + self.dt)]
        for i in range(1, self.point_count - 1):
            a.append(gamma * self.sigma)
            c.append(1 + 2 * gamma * self.sigma)
            b.append(gamma * self.sigma)
            f.append(self.solution[i] + (1 - self.sigma) * gamma *
                     (self.solution[i - 1] - 2 * self.solution[i] + self.solution[i + 1]) +
                     self.dt * self.task.f(self.linspace[i], self.time + self.dt))

        a.append(0)
        c.append(1)
        b.append(0)
        f.append(self.task.mu2(self.time + self.dt))
        solution = np.array(solve_matrix(self.point_count - 1, a, b, c, f))

        return solution



class Implicit_Linear(BaseSolver): #Чисто неявная линейная
    

    def __init__(self, task, interval, eps):
        super().__init__(task, interval, eps)

    def next(self):
        
        a = [0]
        c = [1]
        b = [0]
        f = [self.task.mu1(self.time + self.dt)]

        g = lambda j: 0.5 * (self.task.k(self.solution[j - 1]) + self.task.k(self.solution[j]))

        for i in range(1, self.point_count - 1):
            a.append(self.dt * g(i))
            c.append(self.dx ** 2 + self.dt * (g(i + 1) + g(i)))
            b.append(self.dt * g(i + 1))
            f.append(self.dt * self.dx ** 2 * self.task.f(self.solution[i]) +
                     self.dx ** 2 * self.solution[i])

        a.append(0)
        c.append(1)
        b.append(0)
        f.append(self.task.mu2(self.time + self.dt))

        solution = np.array(solve_matrix(self.point_count - 1, a, b, c, f))

        return solution


    

class Implicit_NonLinear(BaseSolver):#Чисто неявная нелинейная

    def __init__(self, task, interval, eps):
        super().__init__(task, interval, eps)
        self.M = 3 # iterate for M = 3 steps

    def next(self):
        temp_solution = self.solution
        for s in range(self.M):
            a = [0]
            c = [1]
            b = [0]
            f = [self.task.mu1(self.time + self.dt)]

            g = lambda j: 0.5 * (self.task.k(temp_solution[j - 1]) + self.task.k(temp_solution[j]))

            for i in range(1, self.point_count - 1):
                a.append(self.dt * g(i))
                c.append(self.dx ** 2 + self.dt * (g(i + 1) + g(i)))
                b.append(self.dt * g(i + 1))
                f.append(self.dt * self.dx ** 2 * self.task.f(temp_solution[i]) + self.dx ** 2 * self.solution[i])

            a.append(0)
            c.append(1)
            b.append(0)
            f.append(self.task.mu2(self.time + self.dt))
            temp_solution = np.array(solve_matrix(self.point_count - 1, a, b, c, f))

        solution = temp_solution
        return solution
