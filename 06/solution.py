#!/usr/bin/python

def chunk(st, n):
   chunks = zip(*[st[i:] for i in range(n)])
   return [*map(len,map(set,chunks))].index(n) + n

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    solution1 = chunk(raw, 4)
    print(solution1)
    solution2 = chunk(raw, 14)
    print(solution2)
