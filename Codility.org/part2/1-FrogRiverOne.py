
def solution(X, A):
    # write your code in Python 2.7
    occurs= [0] * (X+1)
    
    # Count 1+2+3+4+...+X
    s=int(X/2.0*(X+1))
    
    for i in xrange(len(A)):
        x = A[i]
        if occurs[x] == 0:
            occurs[x]=1
            s -= x
        if  s == 0:
            return i
    return -1
