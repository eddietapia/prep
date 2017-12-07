from Node import Node

class Tree():
  def __init__(self):
    self.root = None

  def insert(self, new_item):
    if self.root is None:
      print 'Inserting', new_item, 'into the tree as a root'
      self.root = Node(new_item)
      return
    current = self.root
    while True:
      if new_item < current.data:
        # Go left
        if current.left is None:
          print 'Inserting', new_item, 'into the tree'
          current.left = Node(new_item)
          current.left.parent = current
          return
        else:
          current = current.left
      elif new_item > current.data:
        # Go right
        if current.right is None:
          print 'Inserting', new_item, 'into the tree'
          current.right = Node(new_item)
          current.right.parent = current
          return
        else:
          current = current.right
      else:
        print 'Item is already in the tree'
        return
  
  def find(self, item):
    current = self.root
    while current is not None:
      if current.data == item:
        return current
      elif current.data < item:
        current = current.left
      else:
        current = current.right
    return "Could not find item in the tree"

  def delete(self, item):
    return 'Not implemented yet'


