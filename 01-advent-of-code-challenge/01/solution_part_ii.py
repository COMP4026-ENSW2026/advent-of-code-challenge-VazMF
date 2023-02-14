with open('01-advent-of-code-challenge/01/day2.in') as file:
   calories = [i for i in file.read().strip().split('\n')]

larger = []
sums = 0

for line in calories:
  if line == '':
    larger.append(sums)
    sums = 0
  else:
    sums += int(line)


total_sum = 0
for i in range(3):
  total_sum += max(larger)
  larger.remove(max(larger))

print(total_sum)