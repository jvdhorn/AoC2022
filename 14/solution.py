#!/usr/bin/python

def parse_input(inp):

  coords = [[(*map(int,ent.split(',')),) for ent in line.split('->')]
            for line in inp]
  x_max  = max(x for y,x in sum(coords, [])) + 2
  grid   = [[0]*(x_max * 2 + 1) for row in range(x_max)]
  for line in coords:
    for (a,b), (c,d) in zip(line, line[1:]):
      for x in range(min(b,d), max(b,d)+1):
        for y in range(min(a,c), max(a,c)+1):
          grid[x][y - 500 + x_max] = 1

  return grid, x_max


def drop_sand(grid, pos):

  x, y = pos
  grid[x][y] = 1
  if x < len(grid) - 1:
    for j in (0, -1, 1):
      if not grid[x+1][y+j]:
        grid[x+1][y+j] = 1
        grid[x][y]     = 0
        return drop_sand(grid, (x+1, y+j))

  return grid


def simulate(grid, drop):

  n = 0
  while not any(grid[-1]):
    grid = drop_sand(grid, (0,drop))
    n   += 1

  k = n
  while not grid[0][drop]:
    grid = drop_sand(grid, (0,drop))
    k   += 1
    
  return n - 1, k


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    grid,drop = parse_input(raw)
    sol1,sol2 = simulate(grid, drop)
    print(sol1)
    print(sol2)
