#!/usr/bin/python

def get_score(arg):
   i,j = arg
   return  6 - (ord(i) - ord(j))%3 * 3 + ord(j) - 87

def get_score_2(arg):
   i,j = arg
   k = ~-ord(j) % 3 - 1
   l = -~ord(i) % 3
   m = (ord(j)-88) * 3
   return (k+l)%3 + 1 + m

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    processed = [*map(str.split, raw.splitlines())]
    solution1 = sum(map(get_score, processed))
    print(solution1)
    solution2 = sum(map(get_score_2, processed))
    print(solution2)
