with open('01-advent-of-code-challenge/04/sample.in') as file:
  sectors = [i for i in file.read().strip().split('\n')]

repeated_assignments = 0
treat_sectors = []

for item in sectors:
  treat_sectors.append(item.strip().split(','))

def contain_interval(first_interval, second_interval):
  numbers1 = set(range(int(first_interval.split('-')[0]), int(first_interval.split('-')[1]) + 1))
  numbers2 = set(range(int(second_interval.split('-')[0]), int(second_interval.split('-')[1]) + 1))

  if numbers1.issubset(numbers2) or numbers2.issubset(numbers1):
    return True
  else:
    return False

for sublist in treat_sectors:
  first_interval = sublist[0]
  second_interval = sublist[1]

  if contain_interval(first_interval, second_interval):
    repeated_assignments += 1

print(f'Os intervalos se contém totalmente em {repeated_assignments} pares.')
