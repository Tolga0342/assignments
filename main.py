# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'


# EK 1988 final 

player_0 = 'Ruud Gullit'
player_1 =  'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_0 + ' ' +  str(goal_0) + ',' +  ' ' + player_1 + ' ' + str(goal_1)
report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"


player = "Marco van Basten"
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ') +1 :])


first_name_first_letter = player[:1] 
name_short =f"{first_name_first_letter}.{player[player.find (' '):]}"


chant =f" {first_name}!" * len(first_name)

good_chant = chant[-1] != ' '
print(good_chant)

 



