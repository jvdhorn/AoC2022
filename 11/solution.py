#!/usr/bin/python

import math


class Monkey(object):

  def __init__(self, name):

    self.name      = name
    self.items     = []
    self.inspected = 0

  def test(self, item):

    result = not item % self.div_test
    
    return [self.test_false, self.test_true][result]

  def inspect_items(self):

    while self.items:
      self.inspected += 1
      yield self.operation(self.items.pop(0))

  def copy(self):
 
    new_monkey            = Monkey(self.name)
    new_monkey.__dict__.update(self.__dict__)
    new_monkey.items      = self.items[:]

    return new_monkey


def parse_monkeys(inp):

  monkeys = []

  for line in inp:
    split = line.split()
    if 'Monkey' in split[:1]:
      monk = Monkey(int(split[1][0]))
      monkeys.append(monk)
    elif 'Starting' in split[:1]:
      for item in split[2:]:
        monk.items.append(int(item.strip(',')))
    elif 'Operation:' in split[:1]:
      func     = eval('lambda old:' + ' '.join(split[3:]))
      setattr(monk, 'operation', func)
    elif 'Test:' in split[:1]:
      setattr(monk, 'div_test', int(split[-1]))
    elif 'true:' in split[1:2]:
      setattr(monk, 'test_true', int(split[-1]))
    elif 'false:' in split[1:2]:
      setattr(monk, 'test_false', int(split[-1]))

  return monkeys
      

def simulate(monkeys, rounds, reduce_worry):

  monkeys = [monk.copy() for monk in monkeys]
  mod     = math.prod(monk.div_test for monk in monkeys) * reduce_worry
  for r in range(rounds):
    for monk in monkeys:
      for item in monk.inspect_items():
        item = item // reduce_worry % mod
        monkeys[monk.test(item)].items.append(item)
  
  return math.prod(sorted(monk.inspected for monk in monkeys)[-2:])


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    monkeys   = parse_monkeys(raw)
    solution1 = simulate(monkeys, 20, reduce_worry=3)
    print(solution1)
    solution2 = simulate(monkeys, 10000, reduce_worry=1)
    print(solution2)
