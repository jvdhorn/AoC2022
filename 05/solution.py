#!/usr/bin/python

def parse_input(inp):

  stacks  = [[*''.join(st).strip()[:-1]] for st in [*zip(*inp[:9])][1::4]]
  actions = [[*map(int,ln.split()[1::2])] for ln in inp[10:]]

  return stacks, actions


def solution(stacks, actions, rev=True):

  stacks = [stack[:] for stack in stacks]

  for x, a, b in actions:
    stacks[b-1][:0], stacks[a-1][:x] = stacks[a-1][:x][::1-rev*2], []
  
  return ''.join([*zip(*stacks)][0])


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    stck, act = parse_input(raw)
    solution1 = solution(stck, act, True)
    print(solution1)
    solution2 = solution(stck, act, False)
    print(solution2)
