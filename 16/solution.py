#!/usr/bin/python

def parse_input(inp):

  valves = {ln[1]:
             (int(ln[4].strip('rate=;')), tuple(x.strip(',') for x in ln[9:]))
            for ln in map(str.split, inp)}

  return valves


def bfs(graph):

  all_distances = dict()

  for x in graph:
    all_distances[x] = visited = dict()
    q                = [(x,0)]

    while q:
      pos, dist = q.pop(0)
      visited.update({pos:dist})
      for option in graph[pos][1]:
        if option not in visited: q.append((option, dist+1))

  return all_distances


def sol_1(inp):

  all_distances = bfs(inp)
  record        = 0
  remaining     = {i for i in inp if inp[i][0]} - {'AA'}
  q             = [(0, 'AA', 30, remaining)]

  while q:
    score, position, steps, remaining = q.pop()
    if score > record: record = score
    distances = all_distances[position]
    options   = {i:(steps-distances[i]-1) * inp[i][0]
                 for i in remaining if steps > distances[i]}
    if not sum(options.values()) < record - score:
      for x in options:
        q.append((options[x] + score, x, steps-distances[x]-1, remaining-{x}))

  return record


def sol_2(inp):

  all_distances = bfs(inp)
  record        = 0
  remaining     = {i for i in inp if inp[i][0]} - {'AA'}
  q             = [(0, 'AA', 'AA', 26, 26, remaining)]
  default       = {None: 0}

  while q:
    score, pos_x, pos_y, steps_x, steps_y, remaining = q.pop()
    if score > record: record = score
    dist_x = all_distances[pos_x]
    dist_y = all_distances[pos_y]
    opts_x = {i: (steps_x-dist_x[i]-1) * inp[i][0]
              for i in remaining if steps_x > dist_x[i]} or default
    opts_y = {i: (steps_y-dist_y[i]-1) * inp[i][0]
              for i in remaining if steps_y > dist_y[i]} or default
    if not sum(opts_x.values()) < record - score > sum(opts_y.values()):
      for x in opts_x:
        for y in opts_y:
          if x != y:
            x_left = steps_x - dist_x[x] - 1 if x else steps_x
            y_left = steps_y - dist_y[y] - 1 if y else steps_y
            new_x  = x if x else pos_x
            new_y  = y if y else pos_y
            q.append((score + opts_x[x] + opts_y[y], new_x, new_y,
                      x_left, y_left, remaining-{x,y}))

  return record


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    valves    = parse_input(raw)
    solution1 = sol_1(valves)
    print(solution1)
    solution2 = sol_2(valves)
    print(solution2)
