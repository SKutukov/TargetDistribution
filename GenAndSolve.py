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
  # print "A=",A,"B=",B,"C=",C
   T={0:0} #Hash: biggest value of set for weight - {weight:value}
   Solution={0:[]}
   #Cicle for all targes $\frac{c_i}{a_i}$
   for i in range(0,len(A)):
   #    print C[i],"/",A[i],":",
       T_old=dict(T)  #copy $T_{k-1}$ into $T_{old}$
  #     print T
       #Cicle for all partial summ
       for x in T_old:
           if (x+A[i])<=B:
               if ( (x+A[i] not in T)  or (T[x+A[i]]<T_old[x]+C[i])):
                   T[x+A[i]]=T_old[x]+C[i]
                   Solution[x+A[i]]=Solution[x]+[i]
 #      print "    -->",T
   ResultCost = max(T.values())
   Result = Solution[argmax(T,Solution,C)]
   return (Result, ResultCost)

def generate_and_solve_Task():

    TaskG = TG.TaskGenerator()
    with open('tasks.txt', 'w') as tasks:
        taskL = TaskG.generate_tasks()
        i = 0
        for task in taskL:
            i = i + 1
            tasks.write("Task " + str(i) + ":\n")
            tasks.write('m:' + str(task.m) + ' n:' + str(task.n) + '\n')
            tasks.write('C:' + str(task.C) + '\n')
            tasks.write('D:' + str(task.D) + '\n')
            tasks.write('\n')

    with open('result.txt','w') as results:
        i = 1
        for task in taskL:
            Result, Cost = knapsack_dylp(task.D, task.m, task.C)
            results.write("Task " + str(i) + ":\n")
            results.write(str(Result) + '\n')
            results.write(str(Cost) + '\n')
            i = i + 1
