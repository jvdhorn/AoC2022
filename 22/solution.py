#!/usr/bin/python

def parse_input(inp):

  maze, walk = inp.split('\n\n')

  maze = maze.splitlines()
  pad  = max(map(len, maze))
  maze = ['{:{}}'.format(ln,pad) for ln in maze]

  walk = [int(c) if c.isnumeric() else c for c in
          walk.replace('L',' L ').replace('R',' R ').split() + ['_']]
  walk = list(zip(*[iter(walk)]*2)) # Split in pairs

  return maze, walk


def rot(arr, n=0):

  n %= 4
  
  return [*map(''.join,arr)] if n < 1 else rot([*zip(*arr)][::-1], n-1)


def sol_1(maze, walk):

  mazes = [rot(maze,n) for n in (0,1,2,3)]
  pos   = [0, maze[0].index('.')]
  drc   = 0
  dim   = [len(maze), len(maze[0])]
  
  for steps, turn in walk:
    
    x, y = pos
    row  = [x, dim[drc%2]-y-1, dim[drc%2]-x-1, y][drc]
    col  = [y, x, dim[1-drc%2]-y-1, dim[1-drc%2]-x-1][drc]
    line = mazes[drc][row]
    strp = line.strip()
    blnk = len(line.rstrip()) - len(strp)
    col  = col - blnk
    stps = min(steps, (strp * 2).find('#', col) % (len(strp)*2) - col - 1)
    col  = (col + stps) % len(strp) + blnk
    pos[1-drc%2] = [col, dim[1-drc%2] - col - 1][drc//2] % dim[1-drc%2]

    drc = (drc + 'L_R'.index(turn) - 1) % 4

  return 1000 * (pos[0]+1) + 4 * (pos[1]+1) + drc


def identify_cube(maze, size):

  faces   = range(6)
  f_iter  = iter(faces)
  net     = [[next(f_iter) if c!=' ' else None for c in ln[::size]]
             for ln in maze[::size]]
  cube    = [[None]*4 for i in faces]
  new_net = dict()
  new_fcs = dict()

  for i,row in enumerate(net):
    for j,col in enumerate(row):
      if col is not None:
        new_net[col] = (i,j)
        new_fcs[col] = [line[j*size:][:size] for line in maze[i*size:][:size]]
        for n,x,y in (3, i-1, j), (1, i+1, j), (2, i, j-1), (0, i, j+1):
          if 0 <= x < len(net) and 0 <= y < len(row) and net[x][y] is not None:
            cube[col][n] = net[x][y]

  for a,b,c,d in [f[:] for f in cube]:
    if a != None != b: cube[a][1] = b; cube[b][0] = a
    if a != None != d: cube[a][3] = d; cube[d][0] = a
    if c != None != b: cube[b][2] = c; cube[c][1] = b
    if c != None != d: cube[c][3] = d; cube[d][2] = c

  opposing = set()
  for a,b,c,d in cube:
    if a != None != c: opposing.add(frozenset((a,c)))
    if b != None != d: opposing.add(frozenset((b,d)))
    if None not in (a,b,c,d):
      opposing.add(frozenset(faces) - {a,b,c,d})
  if len(opposing) == 2:
      opposing.add(frozenset(faces) - frozenset.union(*opposing))

  for a, b in opposing:
    common = set(cube[a]) & set(cube[b]) - {None}
    if common:
      n = common.pop()
      x = cube[a].index(n)
      y = cube[b].index(n)
      for i in 0,1,2,3:
        j, k = cube[a][(x+i)%4], cube[b][(y-i)%4]
        cube[a][(x+i)%4] = cube[b][(y-i)%4] = j if j is not None else k
    for face in cube:
      if a in face: face[(face.index(a)+2)%4] = b
      if b in face: face[(face.index(b)+2)%4] = a

  faces  = [val for key, val in sorted(new_fcs.items())]
  net    = [val for key, val in sorted(new_net.items())]
      
  return cube, faces, net
 

def sol_2(maze, walk):

  size = int((len(''.join(maze).replace(' ',''))//6) ** 0.5)
  cube, faces, net = identify_cube(maze, size)

  f = x = y = d = 0

  for steps, turn in walk:
    for _ in range(steps):
      h, i, j, k = f, x, y, d
      if d%2: i += 1-d//2*2
      else:   j += 1-d//2*2
      if not (0 <= i < size > j >= 0):
        h = cube[f][d]
        k = (cube[h].index(f) + 2) % 4
        t = (k - d) % 4
        if t == 0:
          i = i % size
          j = j % size
        elif t == 2:
          i = (size - i - 1) % size
          j = (size - j - 1) % size
        else: 
          i = [(size - y - 1) % size, y][d%2^t//3]
          j = [(size - x - 1) % size, x][d%2^t//3]
        
      if faces[h][i][j] != '#': f, x, y, d = h, i, j, k
      else                    : break
        
    d = (d + 'L_R'.index(turn) - 1) % 4

  i, j = net[f]

  return 1000 * (i*size+x+1) + 4 * (j*size+y+1) + d


if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    maze,walk = parse_input(raw)
    solution1 = sol_1(maze, walk)
    print(solution1)
    solution2 = sol_2(maze, walk)
    print(solution2)
