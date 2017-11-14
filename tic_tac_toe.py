from IPython.display import clear_output
import random

def display_board(board):
	"""
	Ignoring the zero index to coorelate the placement of 'X's and 'O's with the numpad 1-9 for placement on the board.
	"""
	print('     |     |     ')
	print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  ')
	print('     |     |     ')
	print('=================')
	print('     |     |     ')
	print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '  ')
	print('     |     |     ')
	print('=================')
	print('     |     |     ')
	print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  ')
	print('     |     |     ')
		
		
def player_input():
	xo = ''
	while not (xo == 'X' or xo == 'O'):
		xo = input('Player 1, do you want to be "X" or "O": ').upper()
	if xo == 'X':
		return ('X','O')
	else:
		return ('O','X')
	
def place_marker(board,marker,position):
	board[position] = marker

def win_check(board,mark):
	check_win = False
	for i in range (1,10,3):
		if board[i] == mark and board[i+1] == mark and board[i+2] == mark:
			check_win = True
			break
		elif i == 1 and board[i] == mark and board[i+4] == mark and board[i+8] == mark:
			check_win = True
			break
		elif i == 7 and board[i] == mark and board[i-2] == mark and board[i-4]  == mark:
			check_win = True
			break
		elif i == 7:
			for j in range(7,10):
				if board[j] == mark and board[j-3] == mark and board[j-6] == mark:
					check_win = True
			break
		else:
			check_win = False
	return check_win

def choose_first():
	if random.randint(0,1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board,position):
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True

def player_choice(board):
	while True:
		try:
			position = int(input('Enter position (1-9): '))
			if 0 < position < 10 and space_check(board, position):
				break
		except:
			continue
	return position

def replay():
	replay = ''
	while not (replay == 'Y' or replay == 'N'):
		replay = input('Do you want to play again (Y/N): ').upper()
	return replay.startswith('Y')


print('Welcome to Tic Tac Toe!')
while True:
	board = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print(turn + ' will go first!')
	
	game_on = True
	
	while game_on:
		if turn == "Player 1":
			display_board(board)
			position = player_choice(board)
			place_marker(board, player1_marker, position)
	
			if win_check(board,player1_marker):
				display_board(board)
				print('Congratulations! Player 1, won the game.')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The game is a draw.')
					break
				else:
					turn = 'Player 2'
		else:
			while True:
				position = random.randint(1,9)
				if space_check(board,position):
					break
			place_marker(board, player2_marker, position)
						
			if win_check(board,player2_marker):
				display_board(board)
				print('Congratulations! Player 2, won the game.')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The game is a draw.')
					break
				else:
					turn = 'Player 1'
	if not replay():
		break
				
				
				
				
				
				