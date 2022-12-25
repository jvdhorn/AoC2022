#!/usr/bin/python

def deci(lst):

  return sum(n*5**i for i,n in enumerate(lst[::-1]))


def snafu_to_decimal(snafu):

  conv = {'=':-2, '-':-1, '0': 0, '1':1, '2':2}

  return deci([*map(conv.get, snafu)])


def decimal_to_snafu(number):
  
  num = abs(number)
  lim = [2]

  while deci(lim) < num: lim.append(2)

  for n in range(len(lim)):
    lim[n] = next(i for i in (-2,-1,0,1,2) if deci(lim[:n]+[i]+lim[n+1:])>=num)

  if num == -number:
    lim = [-i for i in lim]

  return ''.join('012=-'[i] for i in lim)


def solutiom(inp):

  total = sum(map(snafu_to_decimal, inp))

  return decimal_to_snafu(total)


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    solution1 = solutiom(raw)
    print(solution1)
