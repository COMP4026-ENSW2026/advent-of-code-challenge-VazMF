with open('01-advent-of-code-challenge/02/sample.int', 'r') as file:
  lines = file.readlines()
  cheats = [entry.strip() for entry in lines]

shape_per_symbol = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_result = {'Lose': 0, 'Draw': 3, 'Win': 6}

score = 0

def game(cheat):
  enemy_shape = shape_per_symbol[cheat[0]]
  player_shape = shape_per_symbol[cheat[2]]

  if player_shape == enemy_shape:
    return points_per_result['Draw'] + points_per_shape[player_shape]
  elif (enemy_shape, player_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
    return points_per_result['Lose'] + points_per_shape[player_shape]
  else:
    return points_per_result['Win'] + points_per_shape[player_shape]


score = sum([game(cheat) for cheat in cheats])
print(f'Your total score is {score}')