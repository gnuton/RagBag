import random

def insertionSort(B):
  # 0(n^2)
  # list divided in left (sorted) and right (unsorted)
  # Takes first from input list and insert it in the left one
  A=B[:]
  n=len(A)
  k=0
  # takes first from right
  for i in xrange(1,n):
    # j goes backward to left from i to 1
    for j in xrange(i, 0, -1):
      if A[j] < A[j-1]: # <-- stable not change order of equal elements
        A[j],A[j-1] = A[j-1],A[j]
      else:
        break
    #print "i=%i j=%i A=%s" %(i,j,str(A))
  return A

def selectionSort(B):
  # worst O(n^2)
  # list is devided in:
  # left - sorted
  # right - unsorted
  # Algo finds smaller on the right one
  # and add it swaps it with the right-most element on the left part
  A=B[:]
  n=len(A)
  for i in xrange(n):
    k=i
    for j in xrange(i+1,n):
      if A[j] < A[k]:
        k=j
    if A[i] != A[k]:  #This make it stable, but by default it's not!
      A[i],A[k] = A[k],A[i]
  return A

def bubbleSort(B):
  # worst O(N^2)
  # it swaps adjacent items.
  # Algo terminates when there are no swap in a complete pass (from 0 to N-1)
  A=B[:]
  n=len(A)
 
  while True:
    swaps=0
    for i in xrange(1,n):
      if A[i] < A[i-1]: #STABLE 
        A[i],A[i-1]=A[i-1],A[i] # require a lot of swaps!
        swaps+=1
    if not swaps:
       break
  return A

def mergeSort(B):
  # Simple O(n lgn) algo
  # Phase 1: divide  - it halves the array and apply mergeSort to each half recoursively
  # Phse  2: conquer - it merges each sorted half
  # Stable, Space comp O(n)
  # edge cases
  if len(B) <= 1:
    return B

  A=B[:]

  # divide
  m=len(A)/2 # elem in the middle
  #print "left=%s right=%s" %(str(A[:m]), str(A[m:]))
  left=mergeSort(A[:m])
  right=mergeSort(A[m:])
  
  # conquer
  A=[]
  while len(left) or len(right):
    if len(left) and len(right):
      if left[0] < right[0]:
        A.append(left.pop(0))
      else:
        A.append(right.pop(0))
    elif not len(left):
        A.append(right.pop(0))
    elif not len(right):
        A.append(left.pop(0))

  return A
  
def quickSort(B):
  # worst/best/average = O(n^2)/O(nlogn)/O(nlogn)
  # space complexity = O(n)
  # not stable
  # 1. choose random pivot
  # 2. creates two arrays with value lower and greater than pivot
  # 3. repeat 1
  # 4. return less + pivots + more lists

  A=B[:]
  
  if len(A) <= 1:
    return A

  pivotIdx= random.randint(0,len(A)-1)
  less, more, n_pivots = [], [], 0 
  for i in xrange(len(A)):
     if A[i] < A[pivotIdx]:
       less.append(A[i])
     elif A[i] > A[pivotIdx]:
        more.append(A[i])
     else:
        n_pivots+=1
  less = quickSort(less)
  more = quickSort(more)
  return less + ([A[pivotIdx]]*n_pivots) + more

# TESTS
algos=[insertionSort, selectionSort, bubbleSort, mergeSort, quickSort]

for sortingAlgo in algos:
  print "Testing: %s" % sortingAlgo.__name__
  R=range(10)
  R=R*2
  R.sort(reverse=True)
  AS = [[], [1], [1,0], [0,2,3,4,5], [random.randint(0,10) for x in xrange(10)], R]
  for A in AS:
    print "Input %s" % str(A)
    B=A[:]
    B.sort()
    sortedA = sortingAlgo(A)
    print "Output %s" % str(sortedA)
    assert sortedA == B
