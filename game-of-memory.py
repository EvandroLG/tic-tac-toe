#!/usr/bin/python

positions_player_one = []
positions_player_two = []

def select_option():
	set_name_player_one()
	set_name_player_two()
	set_option_players()

def set_name_player_one():
	global name_player_one
	name_player_one = raw_input('Name of player 1? ')
	
	if not name_player_one:
		set_name_player_one()

def set_name_player_two():
	global name_player_two
	name_player_two = raw_input('Name of player 2? ')
	
	if not name_player_two:
		set_name_player_two()	

def set_option_players():
	options = ['x', 'o']
	global option_player_one
	option_player_one = raw_input('Player 1 X or O? ')
	
	if option_player_one.lower() in options:
		def set_option_player_two(x):
			if x != option_player_one.lower():
				return x
			
		global option_player_two
		option_player_two = filter(set_option_player_two, options)
		option_player_two = option_player_two[0]
	else:
		set_option_players()
	
def show_table():
	def mark_positions(x):
		if x in positions_player_one:
			x = option_player_one
		elif x in positions_player_two:
			x = option_player_two
		else:
			x = ''
		
		return x

	positions_marked = map(mark_positions, positions)

	print '    A       B       C    '
	print '1   %s  |   %s  |   %s   ' % (positions_marked[0], positions_marked[1], positions_marked[2])
	print '-------------------------'
	print '2   %s  |   %s  |   %s   ' % (positions_marked[3], positions_marked[4], positions_marked[5])
	print '-------------------------'
	print '3   %s  |   %s  |   %s   ' % (positions_marked[8], positions_marked[7], positions_marked[6])

def start_game():
	select_option()
	
	global positions
	positions = {
		'a1': False, 'a2': False, 'a3': False,
		'b1': False, 'b2': False, 'b3': False,
		'c1': False, 'c2': False, 'c3': False
	}
	
	show_table()
	set_positions_player_one()

def set_positions_player_one():
	new_position_player_one = raw_input('Player one, enter a position? ')
	is_position_valid = new_position_player_one in positions and\
						not new_position_player_one in positions_player_one
	
	if is_position_valid:
		positions_player_one.append(new_position_player_one)
		positions[new_position_player_one] = True
		
		show_table()
		congratulations(False)
		
		is_finished = not False in positions.values()
		
		if is_finished:
			congratulations(True)
		else:
			set_positions_player_two()
	else:
		set_positions_player_one()

def set_positions_player_two():
	new_position_player_two = raw_input('Player two, enter a position? ')

	is_position_valid = new_position_player_two in positions and\
						not new_position_player_two in positions_player_two
						
	if is_position_valid:	
		positions_player_two.append(new_position_player_two)
		positions[new_position_player_two] = True
		
		show_table()
		congratulations(False)
		set_positions_player_one()
	else:
		set_positions_player_two()

def congratulations(is_finished):
	name_winner = find_winer()
	message = 'Nobody won!'

	if name_winner:
		message = 'Congratulations, %s! You won!' % (name_winner)
	
	should_display_message = is_finished or name_winner

	if should_display_message:
		print message
		exit()
		
def find_winer():
	combination_one = ['a1', 'a2', 'a3']
	combination_two = ['b1', 'b2', 'b3']
	combination_three = ['c1', 'c2', 'c3']
	combination_four = ['a1', 'b1', 'c1']
	combination_five = ['a2', 'b2', 'c2']
	combination_six = ['a3', 'b3', 'c3']
	combination_seven = ['a1', 'b2', 'c3']
	combination_eight = ['a3', 'b2', 'c1']
	name_winner = None

	is_player_one_winner = set(combination_one) == set(positions_player_one).intersection(combination_one) or\
					       set(combination_two) == set(positions_player_one).intersection(combination_two) or\
				           set(combination_three) == set(positions_player_one).intersection(combination_three) or\
					       set(combination_four) == set(positions_player_one).intersection(combination_four) or\
					       set(combination_five) == set(positions_player_one).intersection(combination_five) or\
					       set(combination_six) == set(positions_player_one).intersection(combination_six) or\
					       set(combination_seven) == set(positions_player_one).intersection(combination_seven) or\
					       set(combination_eight) == set(positions_player_one).intersection(combination_eight)
				
	is_player_two_winner = set(combination_one) == set(positions_player_two).intersection(combination_one) or\
						   set(combination_two) == set(positions_player_two).intersection(combination_two) or\
				           set(combination_three) == set(positions_player_two).intersection(combination_three) or\
					       set(combination_four) == set(positions_player_two).intersection(combination_four) or\
					       set(combination_five) == set(positions_player_two).intersection(combination_five) or\
					       set(combination_six) == set(positions_player_two).intersection(combination_six) or\
					       set(combination_seven) == set(positions_player_two).intersection(combination_seven) or\
					       set(combination_eight) == set(positions_player_two).intersection(combination_eight)
	
	if is_player_one_winner:
		name_winner = name_player_one
	elif is_player_two_winner:
		name_winner = name_player_two
	
	return name_winner
		
def main():
	start_game()
	
if __name__ == '__main__':
	main()