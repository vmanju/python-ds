#!/usr/bin/python

import time
from random import randrange

def find_min1(list_num):
  for i in list_num:
    for j in list_num:
      if i > j:
        min = j
        i = min
  return min


def find_min2(list_num):
  min = list_num[0]
  for i in list_num:
    if i < min:
      min = i
  return min

def benchmark():
  for listSize in range(1000,10001,1000):
    alist = [randrange(10000) for x in range(listSize)]
    start = time.time()
    print find_min1(alist)
    end = time.time()
    print "size: %d time: %f" % (listSize, end-start)

def main():
  #print find_min1([1,3,4,-5,-10])
  #print find_min2([-10,3,-4,5,0])
  benchmark()


if __name__ == "__main__":
  main()
