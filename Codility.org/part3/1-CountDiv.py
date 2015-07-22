
import math
def solution(A, B, K):
    if B-A ==0:
        return int(not bool(A%K))
    else:
        return int(math.ceil((B-(A-1))/float(K)))
