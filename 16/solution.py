#!/usr/bin/python

def parse_input(inp):

  valves = {ln[1]:
             (int(ln[4].strip('rate=;')), tuple(x.strip(',') for x in ln[9:]))
            for ln in map(str.split, inp)}

  return valves


def bfs(x, graph):

  visited = dict()
  q       = [(x,0)]

  while q:
    pos, dist = q.pop(0)
    visited.update({pos:dist})
    for option in graph[pos][1]:
      if option not in visited: q.append((option, dist+1))

  return visited


def sol_1(inp):

  all_distances = {x:bfs(x, inp) for x in inp}
  record        = 0
  remaining     = {i for i in inp if inp[i][0]} - {'AA'}
  q             = [(0, 'AA', 30, remaining)]

  while q:
    score, position, steps, remaining = q.pop()
    if score > record: record = score
    distances = all_distances[position]
    for x in remaining:
      d = distances[x]
      if steps > d:
        q.append(((steps-d-1) * inp[x][0] + score, x, steps-d-1, remaining-{x}))

  return record


def sol_2(inp):

  all_distances = {x:bfs(x, inp) for x in inp}
  record        = 0
  remaining     = {i for i in inp if inp[i][0]} - {'AA'}
  q             = [(0, 'AA', 'AA', 26, 26, remaining)]

  while q:
    score, pos_x, pos_y, steps_x, steps_y, remaining = q.pop()
    if score > record: record = score
    dist_x = all_distances[pos_x]
    dist_y = all_distances[pos_y]
    for x in {i for i in remaining if steps_x > dist_x[i]} or {None}:
      for y in {i for i in remaining if steps_y > dist_y[i]} or {None}:
        if x==y: continue
        elif x==None:
          dy = dist_y[y]
          new_score = (steps_y-dy-1) * inp[y][0] + score
          q.append((new_score, pos_x, y, steps_x, steps_y-dy-1, remaining-{y}))
        elif y==None:
          dx = dist_x[x]
          new_score = (steps_x-dx-1) * inp[x][0] + score
          q.append((new_score, x, pos_y, steps_x-dx-1, steps_y, remaining-{x}))
        else:
          dx = dist_x[x]
          dy = dist_y[y]
          new_score = (steps_x-dx-1) * inp[x][0] + (steps_y-dy-1) * inp[y][0] + score
          q.append((new_score, x, y, steps_x-dx-1, steps_y-dy-1, remaining-{x,y}))

  return record


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    valves    = parse_input(raw)
    solution1 = sol_1(valves)
    print(solution1)
    solution2 = sol_2(valves)
    print(solution2)
