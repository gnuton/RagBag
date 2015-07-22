def counting(A,m):
  """ returns an array with occourences of each item in A
      All the elements are in the set m
  """
  count = [0] * (m+1)
  for x in A:
    count[x] += 1
  
  return count


print counting([1,3,5,2,2,2],5)
