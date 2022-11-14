# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

class Stack:
  def __init__(self) -> None:
    self.stack = []
    self.maximumStack = [None]


  def push(self, val):
    self.stack.append(val)

    if self.maximumStack[-1] == None or self.maximumStack[-1] <= val:
      self.maximumStack.append(val)

  def pop(self):
    value = self.stack.pop()

    if self.maximumStack[-1] == value:
      self.maximumStack.pop()
    return value

  def max(self):
    return self.maximumStack[-1]