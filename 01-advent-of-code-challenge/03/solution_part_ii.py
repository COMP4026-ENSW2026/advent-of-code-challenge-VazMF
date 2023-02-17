with open('01-advent-of-code-challenge/03/sample.in') as file:
   supplies = [i for i in file.read().strip().split('\n')]

sum = 0

while len(supplies) > 0:
  first_part = set(supplies.pop())
  second_part = set(supplies.pop())
  third_part = set(supplies.pop())

  repeated_char = ((first_part.intersection(second_part)).intersection(third_part)).pop()

  if repeated_char.isupper():
    sum += ord(repeated_char) - ord('A') + 27
  else:
    sum += ord(repeated_char) - ord('a') + 1

print(sum)