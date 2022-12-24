#!/usr/bin/python

def parse_input(inp):

  h, w   = len(inp)-2, len(inp[0])-2
  lcm    = min({i*w for i in range(1,h+1)} & {j*h for j in range(1,w+1)})
  states = [set() for _ in range(lcm)]
  moves  = {'>':(0,1), 'v':(1,0), '<':(0,-1), '^':(-1,0)}

  for i, row in enumerate(inp[1:-1]):
    for j, col in enumerate(row[1:-1]):
      if col in '>v<^':
        x, y = moves[col]
        for n in range(lcm):
          states[n].add(((i+x*n)%h, (j+y*n)%w))

  return (h, w), states


def simulate(dims, states, start, end, time):

  h, w    = dims
  l       = len(states)
  states  = states[time%l:]+states[:time%l-l]
  queue   = {(t,)+start for t, state in enumerate(states) if start not in state}
  visited = set()

  while queue:
    pos     = min(queue)
    queue.remove(pos)
    t, x, y = pos
    if (x,y) == end: return t + 1
    visited.add((t%l, x, y))
    for i, j in ((x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1)):
      in_bounds = h > i >= 0 <= j < w
      unvisited = ((t+1)%l, i, j) not in visited
      blizzsafe = (i, j) not in states[(t+1)%l]
      if in_bounds and unvisited and blizzsafe:
        queue.add((t+1, i, j))


def solution(inp):

  (x,y), states = inp
  t0 = simulate((x,y), states, (0,0), (x-1, y-1), 0)
  t1 = simulate((x,y), states, (x-1, y-1), (0,0), t0)
  t2 = simulate((x,y), states, (0,0), (x-1, y-1), t0+t1) 

  return t0, t0+t1+t2


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    parsed    = parse_input(raw)
    sol1,sol2 = solution(parsed)
    print(sol1)
    print(sol2)
