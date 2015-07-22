def solution(A):
    max_ending, max_slice = 0, 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        print "%i %i %i" %(a, max_ending, max_slice)
    return max_slice