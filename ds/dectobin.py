#!/usr/bin/python

from stack import Stack

def decToBin(num):
  remstack = Stack()
  binstring = ""

  while num > 0:
    remstack.push(num % 2)
    num = num // 2

  while not remstack.isEmpty():
    binstring = binstring + str(remstack.pop())

  return binstring

def main():
  print decToBin(25)

if __name__ == "__main__":
  main()

