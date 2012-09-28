#!/bin/python
import sys

def main():
    (N, K) = tuple( [ int(x) for x in  raw_input().strip().split()] )
    costList = [ int(x) for x in raw_input().strip().split() ]
    costList.sort(reverse=True)

    xflowers = 0
    money = 0
    for cost in costList:
        money += ((xflowers/K)+1)*cost
        xflowers += 1
    print money

if __name__ == "__main__":
    main()




