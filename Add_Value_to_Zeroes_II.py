# Given N Elements (All Zeroes)
# Given Q-queries
# In each query a "start index", an "End Index" and a "value" is given
# Add value to all the index from start index to end Index
# Return final state of the Array

# Eg: [0,0,0,0,0,0,0] ==> Element
#     [[2,3,3],[1,3,1],[4,7,5],[0,4,1]] ==> first value here is the "start-index", second value is the "end-index" and third value here is the "Value" 
   
# Result: [1, 2, 5, 5, 6, 5, 5, 5]
# Note: YOU NEED TO SOLVE THIS IN O(Q+N) Time complexity and not O(Q*N) Time Complexity.


def state_bender(A,Q):
    for i in range(len(Q)):
        A[Q[i][0]]+=Q[i][2]
        if (Q[i][1]+1)<len(A):
            A[Q[i][1]+1]+=-Q[i][2]
    pf=[]
    pf.append(A[0])
    for i in range(1,len(A)):
        pf.append(pf[i-1]+A[i])
    print(pf)
        
        
      
A = [0,0,0,0,0,0,0,0]       
Q = [[2,3,3],[1,3,1],[4,7,5],[0,4,1]]
state_bender(A,Q)


# How to do it?
# The process here changes a little bit.
# You know you have to take prefix here and hence rather than just putting the end index..make the element next to the end element -val
# what i mean is 
# if  start =2
#     end = 3
# and val =3

# How it should generally look like:
#      0 1 2 3 4
# A = [0,0,0,0,0]
# val=[0,0,3,3,0]

# How we are doing it is:
#      0 1 2 3 4
# A = [0,0,0,0,0]
#     [_,_,3,_,-3]
# pf= [0,0,3,3,0]
  
  
