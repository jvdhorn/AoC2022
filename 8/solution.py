#!/usr/bin/python

import math

def rot(arr, n=0):

  n %= 4
  
  return arr if n < 1 else rot(zip(*[*arr][::-1]), n-1)

    
def get_vis(line):
  
  return tuple(ch>max(line[:i]or['/']) for i,ch in enumerate(line))


def get_view(line):

  views = ([x>=ch for x in line[i+1:]] for i,ch in enumerate(line))

  return tuple(v.index(True) + 1 if any(v) else len(v) for v in views)


def solution(arr, i):

   a, b, c   = [(get_vis, any, sum), (get_view, math.prod, max)][i-1]
   all_sides = (sum(rot(map(a, rot(arr, n)), -n), ()) for n in range(4))
   score     = c(map(b,zip(*all_sides)))

   return score


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    solution1 = solution(raw, 1)
    print(solution1)
    solution2 = solution(raw, 2)
    print(solution2)

