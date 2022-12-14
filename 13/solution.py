#!/usr/bin/python

def parse_input(inp):

  return [Cmp(eval(lst)) for lst in inp if lst]


class Cmp(list):

  def __lt__(self, other):

    for x, y in zip(self, other):
      if type(x) == type(y) == int:
        if x != y: return x < y
      else:
        if   type(x) == int: x = [x]
        elif type(y) == int: y = [y]
        result = Cmp(x) < Cmp(y)
        if result is not None: return result
    if len(self) != len(other): return len(self) < len(other)


def sol_1(inp):

  pairs = zip(*[iter(inp)]*2)

  return sum(n+1 for n, (a,b) in enumerate(pairs) if a < b)


def sol_2(inp):

  insert = [[[2]], [[6]]]
  x, y = map(sorted(insert + inp).index, insert)

  return (x+1) * (y+1)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    lists     = parse_input(raw)
    solution1 = sol_1(lists)
    print(solution1)
    solution2 = sol_2(lists)
    print(solution2)
