
with open('01-advent-of-code-challenge/06/sample.in') as file:
  buffer = [i for i in file.read().strip()]

characters_number = 0

for i in range(len(buffer)):
  if len(set(buffer[i:i+14])) == 14:
    characters_number = i+14
    break

print(f'É necessário processar {characters_number} caracteres.')
