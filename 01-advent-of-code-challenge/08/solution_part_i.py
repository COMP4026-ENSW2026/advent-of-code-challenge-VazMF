import numpy as np

with open('01-advent-of-code-challenge/08/sample.in') as file:
  lines = file.readlines()
  lines = [entry.strip() for entry in lines]

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
  trees[i, :] = np.array(list(line))

visible = 2 * len(lines[0]) + 2 * (len(lines) -2)

for i in range(1, trees.shape[0]-1):
  for x in range(1, trees.shape[1] - 1):
    column = trees[:, x] - trees[i, x]
    row = trees[i, :] - trees[i, x]

    routes = [row[:x], row[x + 1:], column[:i], column[i + 1:]]
    
    if sum(list(map(lambda route: (route < 0).all(), routes))) > 0:
      visible += 1

print(f'{visible} árvores são visíveis.')