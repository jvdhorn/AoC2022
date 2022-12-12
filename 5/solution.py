#!/usr/bin/python

sol = 2

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    part_1    = [[*''.join(st).strip()[:-1]] for st in [*zip(*raw[:9])][1::4]]
    part_2    = [[*map(int,ln.split()[1::2])] for ln in raw[10:]]
    for x, a, b in part_2:
      part_1[b-1][:0], part_1[a-1][:x] = part_1[a-1][:x][::sol*2-3], []
    solution = ''.join([*zip(*part_1)][0])
    print(solution)
