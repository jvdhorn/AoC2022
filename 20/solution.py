#!/usr/bin/python

def parse_input(inp):

  return list(map(int, inp))


def sol_1(numbers, times=1):

  N       = len(numbers)
  shuffle = list(range(N))
  for n in shuffle * times:
    i = shuffle.index(n)
    j = (i + numbers[n]) % (N-1) or N
    shuffle[i:i+1], shuffle[j:j] = [], [n]
  result = [numbers[k] for k in shuffle]
  zero   = result.index(0)

  return sum(result[(zero+n)%N] for n in (1000, 2000, 3000))


def sol_2(numbers):

  return sol_1([n * 811589153 for n in numbers], 10)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    numbers   = parse_input(raw)
    solution1 = sol_1(numbers)
    print(solution1)
    solution2 = sol_2(numbers)
    print(solution2)
