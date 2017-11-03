import numpy as np
import random

task_number = 20
min_guns_amount=20
max_guns_amount=100
min_targets_amount=4
max_targets_amount=10
min_cost=5
max_cost=50
min_weight=4
max_weight=10
def generate_tasks(task_number,min_ga,max_ga,min_ta,max_ta,min_c,max_c,min_w,max_w):
    for i in range(0,task_number):
        m=random.randint(min_ga,max_ga)
        n = random.randint(min_ta, max_ta)
        C=[]
        D=[]
        for j in range (0,n):
            C.append(random.randint(min_c,max_c))
            D.append(random.randint(min_w, max_w))
        print ("Task ", i, ":")
        print(m,' ', n)
        print(C)
        print(D)
        print("end")

generate_tasks(task_number,min_guns_amount,max_guns_amount,min_targets_amount,max_targets_amount,min_cost,max_cost,min_weight,max_weight)

maxD = 20
n = 4
C = np.array([40, 45, 32, 14])
D = np.array([5, 9, 8, 7])
F=np.zeros((4,20))
#print(maxD)
#print(n)
#print(C)
#print(D)
#print(F)

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
               if (not T.has_key(x+A[i])) or (T[x+A[i]]<T_old[x]+C[i]):
                   T[x+A[i]]=T_old[x]+C[i]
                   Solution[x+A[i]]=Solution[x]+[i]
 #      print "    -->",T
   ResultCost = max(T.values())
   Result = Solution[argmax(T,Solution,C)]
   return (Result, ResultCost)


Result,Cost=knapsack_dylp(D,maxD,C)

#print(Result)
#print(Cost)