#!/usr/bin/python

def parse_input(inp):

  return {tuple(map(int, ln.split(','))) for ln in inp}


def get_area(inp):

  valid = {(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)} 

  return sum(6 - sum((x-i,y-j,z-k) in valid for i,j,k in inp) for x,y,z in inp)


def solution(inp):

  area = get_area(inp)

  x, y, z = (range(min(r)-1, max(r)+2) for r in zip(*inp))
  out     = {(i,j,k) for i in x for j in y for k in z} - inp
  q       = {min(out)}

  while q:
    i, j, k = q.pop()
    q |= {(i-1,j,k),(i+1,j,k),(i,j-1,k),(i,j+1,k),(i,j,k-1),(i,j,k+1)} & out
    out.remove((i,j,k))

  return area, area - get_area(out)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    coords    = parse_input(raw)
    sol1,sol2 = solution(coords)
    print(sol1)
    print(sol2)
