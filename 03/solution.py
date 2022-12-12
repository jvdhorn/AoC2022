#!/usr/bin/python

def get_prio(char):
  return (ord(char)-96) % 58

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    solution1 = 0
    for line in raw.splitlines():
      size = len(line)//2
      a, b = line[:size], line[size:]
      solution1 += ({*map(get_prio, a)}&{*map(get_prio, b)}).pop()
    print(solution1)
    *groups, = zip(*[iter(raw.splitlines())]*3)
    solution2 = 0
    for group in groups:
      a,b,c = map(set, group)
      solution2 += get_prio((a&b&c).pop())
    print(solution2)
