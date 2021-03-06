import random
import task as TaskClass
import numpy as np

class TaskGenerator:
    task_number = 20
    min_ga=20
    max_ga=100
    min_ta=4
    max_ta=10
    min_c=5
    max_c=50
    min_w=4
    max_w=10

    def generate_tasks(self):
        tasks = []
        for i in range(0, self.task_number):
            m = random.randint(self.min_ga, self.max_ga)
            n = random.randint(self.min_ta, self.max_ta)
            C = np.empty(0,dtype=int)
            D = np.empty(0,dtype=int)

            for j in range(0, n):
                C = np.append(C,random.randint(self.min_c, self.max_c))
                D = np.append(D,random.randint(self.min_w, self.max_w))

            task = TaskClass.Task(m, n, C, D)
            tasks.append(task)
        return tasks
