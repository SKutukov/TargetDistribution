
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

