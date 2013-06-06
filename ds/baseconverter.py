#!/usr/bin/python

from stack import Stack

def baseConverter(num, base):
  digits = "0123456789ABCDEF"
  remstack = Stack()
  result = ""

  while num > 0:
    remstack.push(digits[num % base])
    num = num // base

  while not remstack.isEmpty():
    result = result + remstack.pop()

  return result

def main():
  print baseConverter(25,2)
  print baseConverter(25,8)
  print baseConverter(256,16)
  print baseConverter(26,26)

if __name__ == "__main__":
  main()
