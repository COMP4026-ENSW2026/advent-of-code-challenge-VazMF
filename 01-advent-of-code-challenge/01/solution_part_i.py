with open('advent-of-code-challenge-VazMF/01-advent-of-code-challenge/01/sample.in') as file:
   calories = [i for i in file.read().strip().split('\n')]

max = 0
sums = 0

for line in calories:
  if line == '':
    if sums > max:
      max = sums
    sums = 0
  else:
    sums += int(line)

print(sums)
print(max)