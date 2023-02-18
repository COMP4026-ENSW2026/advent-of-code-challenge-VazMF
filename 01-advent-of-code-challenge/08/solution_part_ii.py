import numpy as np

with open('01-advent-of-code-challenge/08/sample.in') as file:
  lines = file.readlines()
  lines = [entry.strip() for entry in lines]

scenic = np.zeros((len(lines), len(lines[0])), dtype=int)

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
  trees[i, :] = np.array(list(line))

def calculate_scenic_score(route):
  larger_trees = list(route >= 0)
  if True in larger_trees:
    return larger_trees.index(True) + 1
  else:
    return len(larger_trees)

for i in range(1, trees.shape[0] - 1):
  for j in range(1, trees.shape[1] - 1):
    
    column = trees[:, j] - trees[i, j]
    row = trees[i, :] - trees[i, j]

    routes = [row[j-1::-1], row[j+1:], column[i-1::-1], column[i+1:]]
    scenic[i,j] = np.prod(list(map(calculate_scenic_score, routes)))

print(f'A maioor pontuação é {np.max(scenic)}.')    