import numpy as np
import TaskGenerator as TG
import task as TaskClass

#task21 = TaskClass.Task(20,4,[40, 45, 32, 14],[5, 9, 8, 7])
#taskL.append(task21)

def argmax(T,Solution,C):
    max_t=0
    max_sum=0
    for t in T:
        S=0
        for i in Solution[t]:
            S=S+C[i]
        if S>max_sum:
            max_sum=S
            max_t=t

    return max_t

def knapsack_dylp(A,B,C):
   T={0:0} #Hash: biggest value of set for weight - {weight:value}
   Solution={0:[]}
   #Cicle for all targes $\frac{c_i}{a_i}$
   for i in range(0,A.shape[0]):
   #    print C[i],"/",A[i],":",
       T_old=dict(T)  #copy $T_{k-1}$ into $T_{old}$
  #     print T
       #Cicle for all partial summ
       for x in T_old:
           if (x+A[i])<=B:
               if (not i in Solution[x]):
                if ( (x+A[i] not in T)  or (T[x+A[i]]<T_old[x]+C[i])):
                   T[x+A[i]]=T_old[x]+C[i]
                   Solution[x+A[i]]=Solution[x]+[i]
 #      print "    -->",T
   ResultCost = max(T.values())
   Result = Solution[argmax(T,Solution,C)]
   return (Result, ResultCost)

def get_tasks_from_file():
    with open('tasks.txt','r') as input:
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

def generate_tasks():
    TaskG = TG.TaskGenerator()
    with open('tasks.txt', 'w') as tasks:
        taskL = TaskG.generate_tasks()
        i = 0
        for task in taskL:
            i = i + 1
            tasks.write("Задание " + str(i) + ":\n")
            tasks.write('m: ' + str(task.m) + ' n: ' + str(task.n) + '\n')
            tasks.write('C:' + str(task.C) + '\n')
            tasks.write('D:' + str(task.D) + '\n')
            tasks.write('\n')
def solve_task():
    task_from_file = get_tasks_from_file()
    with open('result.txt','w') as results:
        i = 1
        for task in task_from_file:
            Result, Cost = knapsack_dylp(task.D, task.m, task.C)
            for i in range(0,len(Result)):
                Result[i] = Result[i] + 1
            results.write("Задание " + str(i) + ":\n")
            results.write(str(Result) + '\n')
            results.write(str(Cost) + '\n')
            results.write('\n')
            i = i + 1
