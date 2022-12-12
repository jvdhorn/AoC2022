#!/usr/bin/python

def get_register(inp):

  cumsum = [1]
  for cmd, *arg in map(str.split, inp):
    prev = cumsum[-1]
    cumsum.append(prev)
    if cmd == 'addx': cumsum.append(prev + int(arg[0]))

  return cumsum


def sol_1(reg):
  
  return sum((a+1)*b for a,b in enumerate(reg) if (a+1)%40 == 20)


def sol_2(reg):

  processed = ('.#'[b-1<=a%40<=b+1] for a,b in enumerate(reg))
  result    = '\n'.join(map(''.join,zip(*[processed]*40)))

  return result


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    register  = get_register(raw)
    solution1 = sol_1(register)
    print(solution1)
    solution2 = sol_2(register)
    print(solution2)
