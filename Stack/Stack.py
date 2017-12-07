"""
Name: Stack.py
Author: Eddie Tapia
Purpose: Stack data structure implementation
"""
from Node import Node

class Stack():
  def __init__(self):
    self.top = None

  def push(self, newItem):
    print 'Pushing', newItem, 'into the stack.'
    oldTop = self.top
    self.top = Node(newItem)
    self.top.next = oldTop

  def pop(self):
    if self.top is None: 
      return "Stack is empty"
    print 'Popping', self.top.data, 'from the stack'
    oldTop = self.top
    self.top = self.top.next
    oldTop.next = None

  def peak(self):
    if self.top is None:
      return "Stack is empty."
    print 'Peaking... found', self.top.data, 'on the top of the stack'
    return self.top.data
