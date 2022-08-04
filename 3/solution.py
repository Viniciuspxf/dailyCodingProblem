class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToList(node, position, array):
  if node != None:
    if not position < len(array):
      for i in range(position - len(array) + 1):
        array.append('')
    array[position] = node.val;
    treeToList(node.left, 2*position, array)
    treeToList(node.right, 2*position + 1, array)

def serialize(node):
  array = ['']
  treeToList(node, 1, array)
  del array[0]
  return ')'.join(array)


def listToTree(array, position):
  if position < len(array) and array[position] != '':
    return Node(array[position], listToTree(array, 2*position), listToTree(array, 2*position + 1))
  else: 
    return None

def deserialize(nodeString):
  array = [''] + nodeString.split(')')
  return listToTree(array, 1)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'