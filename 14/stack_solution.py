#!/usr/bin/python

def parse_input(inp):

  grid = set()
  for line in inp:
    parts = [tuple(map(int,coord.split(','))) for coord in line.split('->')]
    grid |= {(x,y) for (a,b), (c,d) in zip(parts, parts[1:])
                   for x in range(min(b,d), max(b,d)+1)
                   for y in range(min(a,c), max(a,c)+1)}

  return grid


class Stack(list):

  def update(self, grid, limit):

    while self and self[-1][0] <= limit:
      x, y = self[-1]
      if   (x+1, y  ) not in grid: self.append((x+1, y  ))
      elif (x+1, y-1) not in grid: self.append((x+1, y-1))
      elif (x+1, y+1) not in grid: self.append((x+1, y+1))
      else: break


def simulate(grid):

  stack = Stack([(0,500)])
  limit = max(next(zip(*grid)))

  n = k = 0
  while stack:
    if not n and stack[-1][0] == limit: n = k
    stack.update(grid, limit)
    grid.add(stack.pop())
    k += 1

  return n-1, k


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    grid      = parse_input(raw)
    sol1,sol2 = simulate(grid)
    print(sol1)
    print(sol2)
