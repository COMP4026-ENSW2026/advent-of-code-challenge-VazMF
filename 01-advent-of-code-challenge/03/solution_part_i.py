with open('01-advent-of-code-challenge/03/sample.in') as file:
   supplies = [i for i in file.read().strip().split('\n')]

total_sum = 0
for item in supplies:
  first_part = set(item[:(len(item))//2])
  second_part = set(item[(len(item))//2:])

  repeated_char = (first_part.intersection(second_part)).pop()

  if repeated_char.isupper():
    total_sum += ord(repeated_char) - ord('A') + 27
  else:
    total_sum += ord(repeated_char) - ord('a') + 1

print(total_sum)
