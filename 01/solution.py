#!/usr/bin/python

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    processed = [[*map(int, line.split())] for line in raw.split('\n\n')]
    solution1 = max(map(sum, processed))
    print(solution1)
    solution2 = sum(sorted(map(sum, processed))[-3:])
    print(solution2)
