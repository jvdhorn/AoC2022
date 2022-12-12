#!/usr/bin/python

def solution(inp, k=2):

  knots = [[(0,0)] for _ in range(k)]

  for d, n in inp:
    for _ in range(int(n)):
      hx, hy = knots[0][-1]
      if   d == 'U': hx -= 1
      elif d == 'D': hx += 1
      elif d == 'L': hy -= 1
      elif d == 'R': hy += 1
      knots[0].append((hx, hy))

      for i, k in enumerate(knots[1:]):
        hx, hy = knots[i][-1]
        tx, ty = k[-1]
        x = hx - tx
        y = hy - ty
        if max(map(abs, (x, y))) > 1:
          tx = tx + (x and [-1,1][x > 0])
          ty = ty + (y and [-1,1][y > 0])
        k.append((tx, ty))

  return len(set(knots[-1]))


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = [*map(str.split, inp.read().splitlines())]
    solution1 = solution(raw, 2)
    print(solution1)
    solution2 = solution(raw, 10)
    print(solution2)
