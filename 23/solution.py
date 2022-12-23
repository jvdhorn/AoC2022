#!/usr/bin/python

def parse_input(inp):

  elves = set()

  for i, row in enumerate(inp):
    for j, col in enumerate(row):
      if col == '#': elves.add(Elf(j-1j*i))

  return elves


class Elf(complex):

  adjacent = (1+1j, 1, 1-1j, -1j, -1-1j, -1, 1j-1, 1j)

  def propose(self, others, order):

    occupied = [self + i in others for i in self.adjacent]
    if any(occupied):
      occupied.append(occupied[0])
      for move in order:
        if not any(occupied[move-1:move+2]):
          return Elf(self + self.adjacent[move])

    return self


def simulate(elves, steps):

  order = (7,3,5,1)
  count = 0

  while count < steps:
    proposals = dict()
    tracker   = dict()
    for elf in elves:
      prop = elf.propose(elves, order)
      if elf != prop:
        proposals[elf] = prop
        tracker[prop]  = tracker.get(prop, 0) + 1
    for elf, prop in proposals.items():
      if tracker[prop] == 1:
        elves.remove(elf)
        elves.add(prop)
    order  = order[1:] + order[:1]
    count += 1

    if not proposals: break

  return count, elves


def sol_1(elves):

  count, elves = simulate(elves.copy(), 10)

  real = [int(elf.real) for elf in elves]
  imag = [int(elf.imag) for elf in elves]

  return (max(real) - min(real) + 1) * (max(imag) - min(imag) + 1) - len(elves)


def sol_2(elves):

  count, elves = simulate(elves.copy(), float('inf'))

  return count


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    elves     = parse_input(raw)
    solution1 = sol_1(elves)
    print(solution1)
    solution2 = sol_2(elves)
    print(solution2)
