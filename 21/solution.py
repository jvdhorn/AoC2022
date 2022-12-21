#!/usr/bin/python

def parse_input(inp):

  monkeys = dict()
  for line in map(str.split, inp):
    monkey = line[0].strip(':')
    if line[1].isnumeric():
      monkeys[monkey] = [int(line[1])]
    else:
      monkeys[monkey] = line[1:]

  return monkeys


def monkey_reduce(monkeys, stop=''):

  operations  = {
    '+': int.__add__,
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__floordiv__,
  }
  monkeys     = {m:a[:] for m,a in monkeys.items()}

  check_again = True

  while check_again:

    changed = False

    for monkey, arg in list(monkeys.items()):
      if len(arg) == 1 and monkey != stop:
        for val in list(monkeys.values()):
          if monkey in val:
            val[val.index(monkey)] = arg[0]
            changed                = True
            del monkeys[monkey]
      elif len(arg) == 3:
        a, op, b = arg
        if type(a) == type(b) == int:
          monkeys[monkey] = [operations[op](a,b)]
          changed         = True

    check_again = changed

  return monkeys


def solution(monkeys):

  monkeys  = monkey_reduce(monkeys, stop='humn')
  root     = monkey_reduce(monkeys, stop='root')['root'][0]
  nxt, val = sorted(monkeys['root'][::2], key=lambda x:isinstance(x, int))
  
  while nxt != 'humn':
    a, op, b = monkeys[nxt]
    if isinstance(a, str):
      nxt = a
      if   op == '/': val = val * b
      elif op == '*': val = val / b
      elif op == '-': val = val + b
      elif op == '+': val = val - b
    else:
      nxt = b
      if   op == '/': val = a / val
      elif op == '*': val = val / a
      elif op == '-': val = a - val
      elif op == '+': val = val - a

  return root, int(val)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    monkeys   = parse_input(raw)
    sol1,sol2 = solution(monkeys)
    print(sol1)
    print(sol2)
