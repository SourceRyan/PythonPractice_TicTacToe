# Define globals
board = []
player = "X"
gameover = False

# Create a 2d Array for Board, based on user input. Also includes code to print board in a neat-looking way, and then returns the Board var. when called.
# Display is bugged for non-3x3 boards currently.
def setupboard():
	num = 1
	x = int(input("How large of a Tic-Tac-Toe game would you like to play? "))
	print ("Your chosen game size (x and y) is: ",x)
	for i in range(x):
		board.append([])
		for j in range(x):
			board[i].append(num)
			num += 1
	#board = [[1,2,3],
	#         [4,5,6],
	#         [7,8,9]]
	if x == 3:
		for i in board:
			for j in i:
				print(j, end = "  ")
			print()
	else:
		for i in board:
			print(j, end = "  ")
	return board

board = setupboard()

# For testing the board list, should return 1 if uncommented
#print(board[0][0])

# Checks for wins, defines row as the length of the board array. Subfunctions check for rows, columns, and diagonal wins.
# Currently, only the Column check seems to be working correctly.
def checkwin(player):
	for x in  range(len(board)):
		check_win_row(x, board, player)
		check_win_col(x, board, player)
	check_win_diag_a(board, player)
	check_win_diag_b(board, player)
	return gameover

# Checks rows for wins
def check_win_row(rownum, daboard, player):
	winrow = True
	for col in range(len(board)): 
		if board[rownum][col] != player:
			winrow = False
			return winrow
	if winrow == True:
		gameover = True
		print ("%s has won the game!" % player)
		exit()
# Check column for wins
def check_win_col(colnum, daboard, player):
	wincol = True
	for row in range(len(board[0])): 
		if board[row][colnum] != player:
			wincol = False
			return wincol
	if wincol == True:
		gameover = True
		print ("%s has won the game!" % player)
		exit()
# Check top-to-bottom diagonal for wins.
def check_win_diag_a(daboard, player):
	windiag_a = True
	for diag_a in range(len(board)):
		if board[diag_a][diag_a] != player:
			windiag_a = False
			return windiag_a
	if windiag_a == True:
		gameover = True
		print ("%s has won the game!" % player)
		exit()
# Check bottom-to-top diagonal for wins.
def check_win_diag_b(daboard, player):
	windiag_b = True
	for diag_b in range(len(board)):
	        # "IndexError: list index out of range" when 9 is selected on a 3x3 board.
			if board[len(board)-diag_b-1][diag_b] != player:
				windiag_b = False
				return windiag_b
	if windiag_b == True:
		gameover = True
		print ("%s has won the game!" % player)
		exit()
# Part of main Loop, select number from 2d Array
while(not gameover):
	try:
		play = int(input("Please pick a number on the board: "))
		if play > len(board)*len(board):
			print ("Your chosen number is invalid, please select another")
			#better try again... Return to the start of the loop
			continue
		if play <= 0:
			print ("Your chosen number is invalid, please select another")
			#better try again... Return to the start of the loop
			continue
		board[int(play/len(board))][play%len(board)-1] = player
	except ValueError:
		print ("Your chosen number is invalid, please select another")
		#better try again... Return to the start of the loop
		continue
		#call checkwin function and switch between players each turn.
	checkwin(player)
	if player == "X":
		player = "Y"
		print ("It is now %s's turn." % player)
		continue
	else:
		player = "X"
		print ("It is now %s's turn." % player)
		continue
exit()
