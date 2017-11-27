import task as TaskClass
import task_solver
import numpy as np
def get_tasks_from_file(filename):
    with open(filename,'r') as input:
        i = 0
        content = input.readlines()
        tasks = []
        for j in range(0, 20):
            #read n and m
            i = i + 1
            line = content[i].split()
            m = int(line[1])
            n = int(line[3])

            def split_np_array(line):
                line = line.split(':')
                line = line[1].split('[')
                line = line[1].split(']')
                return np.fromstring(line[0], dtype=int, sep=' ')

            #read C
            i = i + 1
            C = split_np_array(content[i])

            #read D
            i = i + 1
            D = split_np_array(content[i])

            #construct task
            task = TaskClass.Task(m, n, C, D)
            tasks.append(task)
            #skip empty line
            i = i + 2
        return tasks

def solve_task(result_filename, input_filename ):
    task_from_file = get_tasks_from_file(input_filename)
    with open(result_filename,'w') as results:
        i = 1
        for task in task_from_file:
            Result, Cost = task_solver.knapsack_dylp(task.D, task.m, task.C)
            for j in range(0,len(Result)):
                Result[j] = Result[j] + 1
            results.write("Задание " + str(i) + ":\n")
            results.write(str(Result) + '\n')
            results.write(str(Cost) + '\n')
            results.write('\n')
            i = i + 1