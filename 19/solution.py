#!/usr/bin/python

def parse_input(inp):

  factories = []

  for line in map(str.split, inp):
    n,a,b,c,d,e,f = (int(line[n].strip(':')) for n in (1,6,12,18,21,27,30))
    cost          = ((a,0,0,0), (b,0,0,0), (c,d,0,0), (e,0,f,0))
    factories.append(Factory(n, cost))

  return factories


class Factory(object):

  robots    = (1,0,0,0)
  resources = (0,0,0,0)

  def __init__(self, n, cost):

    self.number = n
    self.cost   = cost

  def simulate(self, time):

    q      = {(time, self.robots, self.resources)}
    geodes = 0

    while q:
      t, robots, res = q.pop()
      q_add          = set()
      for n in 0,1,2,3:
        abc         = list(zip(robots, res, self.cost[n]))
        can_build   = all(c==0 or a for a, b, c in abc)
        time_needed = max(1-((b-c)//a) for a, b, c in abc if a) # Ceil div
        if can_build and 0 < time_needed < t:
          new_robots    = robots[:n] + (robots[n]+1,) + robots[n+1:]
          new_resources = tuple(b + a * time_needed - c for a, b, c in abc)
          q_add.add((t - time_needed, new_robots, new_resources))
      q.update(q_add)
      if not q_add:
        geodes = max(geodes, res[-1] + robots[-1] * t)

    return geodes


def sol_1(factories):

  total = 0
  for f in factories:
    total += f.number * f.simulate(24)

  return total


def sol_2(factories):

  total = 1
  for f in factories[:3]:
    total *= f.simulate(32)

  return total

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    factories = parse_input(raw)
    solution1 = sol_1(factories)
    print(solution1)
    solution2 = sol_2(factories)
    print(solution2)
