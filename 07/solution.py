#!/usr/bin/python

def build_tree(inp):

  tree = dict()
  path = []
  for line in inp.splitlines():
    if line.startswith('$'):
      cmd, *arg = line.split()[1:]
      if cmd == 'cd':
        arg = arg[0]
        if   arg == '/' : path = ['/']
        elif arg == '..': path = path[:-1]
        else            : path = path + [arg]
      elif cmd == 'ls':
        target = tuple(path)
        tree[target] = tree.get(target, [])
      else:
        pass
    else:
      item, name = line.split()
      if item != 'dir':
        tree[target].append((int(item), name))

  return tree
  

if __name__ == '__main__':
  with open('input.txt') as inp:
    raw       = inp.read()
    tree      = build_tree(raw)

    filesizes = dict.fromkeys(tree.keys(), 0)
    for path, files in tree.items():
      size = sum(entry[0] for entry in files)
      for n, directory in enumerate(path):
        filesizes[path[:n+1]] += size

    solution1 = sum(size for size in filesizes.values() if size <= 100_000)
    print(solution1)

    free      = filesizes[('/',)] - 40_000_000
    solution2 = min(size for size in filesizes.values() if size >= free)
    print(solution2)
