# Given N Elements (All Zeroes)
# Given Q-queries
# In each query an "index" and a "value" is given
# Add value to all the index from index I
# Return final state of the Array

# Eg: [0,0,0,0,0] ==> Element
#     [[2,3][1,4][0,6]] ==> first value here is the "index" and second value here is the "Value" 
   
# Result: [6,10,13,13,13]
# Note: YOU NEED TO SOLVE THIS IN O(Q+N) Time complexity and not O(Q*N) Time Complexity.
  
  
  
def state_bender(A,Q):
    for i in range(len(Q)):
        A[Q[i][0]]=Q[i][1]
    pf=[]
    pf.append(A[0])
    for i in range(1,len(A)):
        pf.append(pf[i-1]+A[i])
    print(pf)
        
        
      
A = [0,0,0,0,0]       
Q = [[2,3],[1,4],[0,6]]
state_bender(A,Q)

# How to do it?
# First loop of Q to just "set the value on a particular index"
# Second loop to start using "prefix values from the resultant of the first loop"
