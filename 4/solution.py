#!/usr/bin/python

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    processed = [[[*map(int, x.split('-'))]
                   for x in line.split(',')]
                 for line in raw.splitlines()]
    range_set = [({*range(a,b+1)},{*range(c,d+1)}) for (a,b),(c,d) in processed]
    solution1 = sum(x<=y or y<=x for x,y in range_set)
    print(solution1)
    solution2 = sum(bool(x&y) for x,y in range_set)
    print(solution2)
