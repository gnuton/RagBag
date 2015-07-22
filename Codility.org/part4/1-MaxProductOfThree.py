def solution(A):
    # Trick: [-5,-4,0,1,2] => max is -5 * -4 * 2
    if len(A) < 3:
        return 0
        
    A.sort(reverse=True)
    opz1= A[0]  * A[1] * A[2]
    opz2= A[0]  * A[-1] * A[-2]
    return opz2 if opz2 > opz1 else opz1

# grade https://codility.com/demo/results/demoMERTGB-9T2/
