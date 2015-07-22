def solution(A):
    # write your code in Python 2.7
    
    if len(A) == 0:
      return 0

    A.sort()
    for x in xrange(len(A)):
        if A[x] != x+1:
            return x+1

    return -1 # nothing missing


A=[1,2,3,4]
print solution(A)

A=[1,2,3,0]
print solution(A)

