def solution(A):
    # write your code in Python 2.7

    s = list(set(A))
    s.sort()
    
    prev=0
    for i in s:
      
        if i <= 0:
            continue
        else:
          if i == prev+1:
              prev=i
              continue
          else:
              return prev+1
    return s[-1]+1
