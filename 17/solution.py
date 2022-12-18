#!/usr/bin/python

def get_wind(inp):

  n = 0
  while True:
    yield n, ord(inp[n])-61
    n = (n + 1) % len(inp)


class Rocks(object):

  count = 0
  rocks = (
    {(0,2), (0,3), (0,4), (0,5)},
    {(0,3), (1,2), (1,3), (1,4), (2,3)},
    {(0,2), (0,3), (0,4), (1,4), (2,4)},
    {(0,2), (1,2), (2,2), (3,2)},
    {(0,2), (0,3), (1,2), (1,3)},
  )

  def get(self, h):

    rock       = Rock((x+h, y) for x, y in self.rocks[self.count])
    self.count = (self.count + 1) % len(self.rocks)

    return self.count, rock


class Rock(set):

  def drop(self, grid):

    nxt = {(x-1, y) for x, y in self}
    low = min(next(zip(*nxt)))
    val = (not nxt & grid) and (low >= 0)
    if val:
      self.clear()
      self.update(nxt)
    
    return val


  def push(self, grid, d):

    nxt = {(x, y+d) for x, y in self}
    rng = [*zip(*nxt)][1]
    left, right = min(rng), max(rng)
    val = (not nxt & grid) and (0 <= left <= right <= 6)
    if val:
      self.clear()
      self.update(nxt)

    return val


def vis(grid):

  x = max(next(zip(*grid)))
  for i in range(x+1, -1, -1):
    print('|'+''.join(' #'[(i,j) in grid] for j in range(7))+'|')
  print('+-------+')


def solution(inp, n):

  blow   = get_wind(inp)
  rocks  = Rocks()
  grid   = set()
  height = 0
  diff   = []
  prev   = {}
  rep    = 0

  while not rep:
    r, rock = rocks.get(height + 3)
    drop = 1
    while drop:
      w, wind = next(blow)
      rock.push(grid, wind)
      drop = (drop + 1) * rock.drop(grid)
      if w == 0:
        p = prev.get((r,drop))
        if p: rep = len(diff) - p
        else: prev[(r,drop)] = len(diff)
    new_height = max(next(zip(*rock))+(height-1,)) + 1
    diff.append(new_height - height)
    height     = new_height
    grid      |= rock

  start = len(diff) - rep
  mid   = max(0, n - start) // rep
  end   = n - start - mid * rep

  return sum(diff[:start]) + mid * sum(diff[-rep:]) + sum(diff[-rep:end-rep])


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().strip()
    solution1 = solution(raw, 2022)
    print(solution1)
    solution2 = solution(raw, 1_000000_000000)
    print(solution2)
