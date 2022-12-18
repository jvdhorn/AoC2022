#!/usr/bin/python

def parse_input(inp):

  return {tuple(map(int, ln.split(','))) for ln in inp}


def get_adj(pos):

  i, j, k = pos

  return {(i-1,j,k),(i+1,j,k),(i,j-1,k),(i,j+1,k),(i,j,k-1),(i,j,k+1)}


def sol_1(inp):

  return sum(6 - len(get_adj(pos) & inp) for pos in inp)


def sol_2(inp):

  x, y, z = (range(min(r)-1, max(r)+2) for r in zip(*inp))
  out     = {(i,j,k) for i in x for j in y for k in z} - inp
  q       = {min(out)}

  while q:
    pos = q.pop()
    q.update(get_adj(pos) & out)
    out.remove(pos)

  return sol_1(inp | out)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    coords    = parse_input(raw)
    solution1 = sol_1(coords)
    print(solution1)
    solution2 = sol_2(coords)
    print(solution2)
