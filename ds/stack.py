#!/usr/bin/python

__author__ = "vmanju"

class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)

  def peek(self):
    return self.items[len(self.items)-1]

  def pop(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


def main():
  s = Stack()
  print "Is stack empty?: ", s.isEmpty()
  print "Push 1 ", s.push(1)
  print "Push 2 ", s.push(2)
  print "Push 3 ", s.push(3)
  print "Pop top element", s.pop()
  print "Size of stack: ", s.size()
  print "Top element of stack: ", s.peek()


if __name__ == "__main__":
  main()
