import numpy as np
maxD=20
n=4
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

print(Result)
print(Cost)