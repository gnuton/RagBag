def solution(A):
    # write your code in Python 2.7
    A.sort()
    
    if len(A) < 3:
        return 0
    
    A.sort()
    combinations= [(0,1,2),(0,1,-1),(0,-2,-1),(-3,-2,-1)]
    for p,q,r in combinations:
        if (A[p] + A[q]) > A[r] and (A[q] + A[r]) > A[p] and (A[r] + A[p]) > A[q]:
            return 1
    return 0

# Score https://codility.com/demo/results/demo9TA8JH-DSX/ 
