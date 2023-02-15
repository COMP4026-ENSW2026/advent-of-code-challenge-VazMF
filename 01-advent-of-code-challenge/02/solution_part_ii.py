with open('01-advent-of-code-challenge/02/sample.in', 'r') as file:
  lines = file.readlines()
  cheats = [entry.strip() for entry in lines]

shape_per_symbol = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_result = {'Lose': 0, 'Draw': 3, 'Win': 6}

score = 0

def game(cheat):
  enemy_shape = shape_per_symbol[cheat[0]]
  player_goal = shape_per_symbol[cheat[2]]

  if (enemy_shape, player_goal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
    return points_per_result[player_goal] + points_per_shape['Rock']
  elif (enemy_shape, player_goal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
    return points_per_result[player_goal] + points_per_shape['Paper']
  else:
    return points_per_result[player_goal] + points_per_shape['Scissors']


score = sum([game(cheat) for cheat in cheats])
print(f'Your total score is {score}')