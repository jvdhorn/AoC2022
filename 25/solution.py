#!/usr/bin/python

def snafu_to_decimal(snafu):

  conv = {'=':-2, '-':-1, '0': 0, '1':1, '2':2}

  return sum(conv[n]*5**i for i,n in enumerate(snafu[::-1]))


def decimal_to_snafu(number):
  
  num    = abs(number)
  snafu  = []
  maxpow = 1
  lim    = 2

  while lim < num:
    lim    += 2 * 5 ** maxpow
    maxpow += 1

  for n in range(maxpow - 1, -1, -1):
    lim -= 4 * 5 ** n
    snafu.append(-2)
    while lim < num:
      lim += 5 ** n
      snafu[-1] += 1

  return ''.join('012=-'[i if num == number else -i] for i in snafu)


def solutiom(inp):

  total = sum(map(snafu_to_decimal, inp))

  return decimal_to_snafu(total)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    solution1 = solutiom(raw)
    print(solution1)
