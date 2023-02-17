with open('01-advent-of-code-challenge/04/sample.in') as file:
  sectors = [i for i in file.read().strip().split('\n')]

repeated_assignments = 0
treat_sectors = []

for item in sectors:
  treat_sectors.append(item.strip().split(','))

def check_contain(first_interval, second_interval):
  start1, end1 = map(int, first_interval.split("-"))
  start2, end2 = map(int, second_interval.split("-"))
  return start1 <= end2 and start2 <= end1


for pair in treat_sectors:
  if check_contain(pair[0], pair[1]):
    repeated_assignments += 1
  
print(f'Os intervalos se sobrepõem em {repeated_assignments} pares.')
