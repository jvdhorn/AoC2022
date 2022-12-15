#!/usr/bin/python

def parse_input(inp):

  sensors = [[int(l[i].strip('xy=:,')) for i in (2,3,8,9)]
             for l in map(str.split, inp)]

  return sensors


class Ranges(list):

  def update(self, rng):
    x, y = rng
    for i, j in self[:]:
      if i <= x <= j + 1 or x <= i <= y + 1:
        x, y = min(i,x), max(j,y)
        self.remove((i,j))
    self.append((x,y))


def get_distances(sensors):

  distances = dict()
  for a, b, x, y in sensors:
    dist = abs(a-x) + abs(b-y)
    distances[(a,b)] = dist

  return distances


def sol_1(sensors, n=2000000):

  distances = get_distances(sensors)
  beacons   = len({x for a, b, x, y in sensors if y==n})

  rng = Ranges()
  for x, y in distances:
    dist = distances[(x,y)] - abs(n - y)
    if dist > 0: rng.update((x-dist, x+dist))

  return sum(j-i+1 for i, j in rng) - beacons


def sol_2(sensors, n=4000000):

  distances = get_distances(sensors)

  for i in range(n+1):
    rng = Ranges()
    for x, y in distances:
      dist = distances[(x,y)] - abs(i - y)
      if dist > 0: rng.update((max(0,x-dist), min(n, x+dist)))
    if len(rng) > 1: break
  
  return (min(rng)[1] + 1) * n + i


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    sensors   = parse_input(raw)
    solution1 = sol_1(sensors)
    print(solution1)
    solution2 = sol_2(sensors)
    print(solution2)
