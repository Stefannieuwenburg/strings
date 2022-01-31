# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Voorbeeld string format(f'welkom {str(name)}')


example = 'Gut von Examplestein'
goal_0 = 32

# Part 1
scorer_0 = 'Ruud Gullit '
scorer_1 = 'Marco van Basten '

goal_0 = 32
goal_1 = 54

scorers = f"{scorer_0}{str(goal_0)} , {scorer_1}{str(goal_1)}"
print(scorers)

report = f'{scorer_0} scored in the {str(goal_0)} nd minute  \n{scorer_1} scored in the  {str(goal_1)} th minute'
print(report)

# Part 2
player = 'Ruud Gullit'

first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[(player.find(' ') + 1):])
print(last_name_len)

name_short = (f"{player[0]} .  {player[5:]}")
print(name_short)

chant = ((first_name + '! ') * (len(first_name) - 1)) + first_name + '!'
print(chant)

good_chant = (chant[((len(chant) - 1)):] != '! ')
print(good_chant)
