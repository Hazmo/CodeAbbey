def move(x, mark):
	row = (x - 1) / 3
	col = (x - 1) % 3

	board[row][col] = mark

def checkFor3(list):
		if 0 in list:
			return False
		elif all(x == list[0] for x in list):
			return True
		else:
			list = []
			return False

def checkBoard():
	checkList = []

	for row in range(3):
		if checkFor3(board[row]):
			return 1

	for col in range(3):
		checkList.append(board[0][col])
		checkList.append(board[1][col])
		checkList.append(board[2][col])

		if checkFor3(checkList):
			return 1

	for row, col in zip(range(3), range(3)):
		checkList.append(board[row][col])


	if checkFor3(checkList):
		return 1

	for row, col in zip(range(2, -1, -1), range(3)):
		checkList.append(board[row][col])

		if checkFor3(checkList):
			return 1


	return 0



board = [[0]*3 for x in range(3)]

inputs = int(raw_input())
for _ in range(inputs):
    #Crosses is true, Nought is faslse
    turn = True
    moveNo = 0
    input = [int(x) for x in raw_input().split()]
    
    for playerMove in input:
        if turn:
            move(playerMove, "X")
        else:
            move(playerMove, "O")
            
        moveNo += 1
        turn = not turn
        
        if checkBoard() == 1:
			print moveNo
			break
    	else:
        	print 0
	print board
    print " "
