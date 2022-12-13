#!/usr/bin/python

def parse_input(inp):

  return [*map(eval, inp.replace('\n\n','\n').splitlines())]


def compare(a, b):

  for x, y in zip(a,b):
    if type(x) == type(y) == int:
      if x != y: return x < y
    else:
      if   type(x) == int: x = [x]
      elif type(y) == int: y = [y]
      result = compare(x, y)
      if result is not None:
        return result
  if len(a) != len(b):
    return len(a) < len(b)


def sol_1(inp):

  pairs  = zip(*[iter(inp)]*2)
  result = []
  for n,(a,b) in enumerate(pairs):
    if compare(a,b): result.append(n+1)

  return sum(result)


def sol_2(inp):

  insert = [[[2]], [[6]]]
  result = insert[:]
  for new in inp:
    for n, other in enumerate(result):
      if compare(new, other): break
    else: n = n+1
    result.insert(n, new)
  x, y = map(result.index, insert)

  return (x+1) * (y+1)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    lists     = parse_input(raw)
    solution1 = sol_1(lists)
    print(solution1)
    solution2 = sol_2(lists)
    print(solution2)
