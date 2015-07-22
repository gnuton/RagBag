def solution(A):
    # write your code in Python 2.7
    pairs=0
    n=len(A)
    count=0
    for i in xrange(n):
        count += A[n-i-1]
        if A[n-i-1] == 0:
            pairs+=count
            if pairs > 1000000000:
                return -1
    return pairs
