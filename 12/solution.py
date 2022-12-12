#!/usr/bin/python

def solution(inp, start):

  l = 0
  p = set()
  q = [(x,y,l) for x, row in enumerate(inp)
               for y, col in enumerate(row) if col in start]

  while q:
    x, y, l = q.pop(0)
    char = inp[x][y].replace('S','a')
    if char == 'E': break
    for i, j in (x+1,y), (x-1,y), (x,y+1), (x,y-1):
      if (0 <= i < len(inp) and 0 <= j < len(inp[i]) and (i,j) not in p 
          and (char >= 'y' or 'a' <= inp[i][j] <= chr(ord(char)+1))):
        p.add((i,j))
        q.append((i,j,l+1))

  return l


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read().splitlines()
    solution1 = solution(raw, 'S')
    print(solution1)
    solution2 = solution(raw, 'Sa')
    print(solution2)
