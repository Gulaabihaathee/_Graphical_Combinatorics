import numpy as np

#Ones Counter
def Ones_Counter(GameBoard):
	#Ones Amount for Position(i,j)
	OAPOSij = [] 
	for p in range(0,len(Starting_Positions)):
		i = Starting_Positions[p][0]
		j = Starting_Positions[p][1]
		OAPOSij.append(np.sum(GameBoard[i][j:]) + np.sum(GameBoard.transpose()[j][i+1:]))
	return(OAPOSij)

#Permutations Generator for Starting Positions Tuple
def CrossCombine(St_Pos_List):
	#Knot positions	
	Pos_Moves = [[St_Pos_List]]
	VPM = []
	HPM = []

	#Vertical
	for i in range(St_Pos_List[0]+1, n):
		VPM.append((i, St_Pos_List[1]))
	
	for i in range(1,len(VPM)+1):
		Pos_Moves += [Pos_Moves[0] + VPM[:i]]

	#Horizontal
	for j in range(St_Pos_List[1]+1, n):
		HPM.append((St_Pos_List[0],j))	

	for i in range(1,len(HPM)+1):
		Pos_Moves += [Pos_Moves[0] + HPM[:i]]	

	return(Pos_Moves)

#GameBoard Moves(All Possibilities From Every Positions)
def GameMoves(Starting_Positions):
	Game_Moves = []	
	for tup in Starting_Positions:
		if(GameBoard[tup[0]][tup[1]] == 1):
			Game_Moves.append(CrossCombine(tup))
	return(Game_Moves)

#GM = GameMoves(SPGenerator(n))
#Function Excluding GameMoves with zero(empty place instead a ball)
def ZeroCutter(GM):
	for moves in range(0, len(GM)):
		for move in range(0, len(GM[moves])):
			for tup in range(0, len(GM[moves][move])):		
				if(GameBoard[GM[moves][move][tup][0]][GM[moves][move][tup][1]] == 0):
					GM[moves][move][tup] = ()
	
	for i in range(0, len(GM)):
		for j in range(0, len(GM[i])):
			GM[i][j] = list(filter(None, GM[i][j]))


	for i in range(0, len(GM)):
		GM[i] = list(map(list,list(set(map(tuple, GM[i])))))

	return(GM)


#Show possible moves in coordinates(i,j) from ball in position of 1st tuple 
def ShowMoves(GM):
	index = 0
	for i in GM:
		for j in i:
			index+=1
			print("----",index," ", j)
		print("*******************")

#How to forbid crossing out last element?
def IsThisTheEnd(GameBoard):
	if(np.sum(GameBoard) == 1):
		return(1)
	else:
		return(0)

#GameBoard creation
def CreateGameBoard(n):
	return(np.array([[1]*n]*n))

#Returns the list of GameBoards with every possible move
def Scenarios_for_Game(GM):
	it = 0
	ScenarioTable = []
	for i in GM:
		for j in i:
			ScenarioTable.append(CreateGameBoard(n))
			for k in j:
				ScenarioTable[it][k[0]][k[1]] = 0		
			it += 1
	return(ScenarioTable)

#Algorithm Positions Generator 
def PGenerator(n, GameBoard):
	#Algorithm Starting Positions
	Positions = []
	
	for i in range(0,n):
		for j in range(0,n):
			if(GameBoard[i][j] == 1):
				Positions.append((i,j))
	return(Positions)

#___________________________________________________________________________
#---------------------------------------------------------------------------
#___________________________________________________________________________


n = 4
GameBoard = CreateGameBoard(n)
GM = GameMoves(PGenerator(n, GameBoard))
SC = Scenarios_for_Game(GM)

"""
#All Possible Moves Amount for current GameBoard
PMA = np.sum(Ones_Counter(GameBoard))

#Ones Counter List (V+H elements)
OC_List = Ones_Counter(GameBoard)


"""
