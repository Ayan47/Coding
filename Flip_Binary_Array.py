# Q: Given a binary Array of 0's and 1's
# You are allowed to perform atmost 1 operation.
# Flip the values of the subarray and find the Max no. of 1's in there.


# Algo: Kadane's Algorithm.
# Process:  Convert the existing 0's to 1's
#           Convert the existing 1's to -1's
#           Keep count of the Existing 1's
#           run Kadane's algorithm ( if sum is -ve make the sum 0 else count them up and find max)
#           return count of existing 1's + max sum value 

def find_max_ones(A):
    overall = 0
    countone=0
    maxval=0
    for i in range(len(A)):
        if A[i]==0:
            A[i]=1
        else:
            A[i]=-1
            countone+=1
    for i in range(len(A)):
        overall+=A[i]
        if overall<0:
            overall=0
        if overall>maxval:
            maxval=overall
    return(maxval+countone)




A = [1,0,1,1,0,0,1]
print(find_max_ones(A))
B = [0,0,0,1,1,0,0,0,1]
print(find_max_ones(B))
