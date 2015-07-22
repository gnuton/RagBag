class stack(list):
  """ LILO
  """ 
  def push(self, x):
    self.append(x)
    
  def pop(self):
    return super(stack, self).pop()

class queue(list):
  """ FIFO
  """
  def push(self,x):
    self.append(x)

  def pop(self):
    return super(queue,self).pop(0)

s = stack()
s.push(1)
s.push(2)
s.push(3)
assert s.pop() == 3
assert len(s) == 2 

q = queue()
q.push(1)
q.push(2)
q.push(3)
assert q.pop() == 1
assert len(s) == 2

print "all done! No errors!"
