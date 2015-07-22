# you can use print for debugging purposes, e.g.
# print "this is a debug message"



def solution(A):
    M=len(set(A))
    N=len(A)
    if M != N:
        return 0
    # sum of 1+2+3+4+...+N
    s=int(N/2.0*(N+1))
    return int(sum(A) == s)
