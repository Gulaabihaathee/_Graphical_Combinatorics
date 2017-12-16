import numpy as np
import copy

#Ones Counter List (V+H elements)
def Ones_Counter(GameBoard):
	#Ones Amount for Position(i,j)
	Starting_Positions = PGenerator(GameBoard)
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

#GM = GameMoves(PGenerator(n, GameBoard))
#Function Excluding GameMoves with zero(empty place instead a ball)
#Updated cutting zeros for given GameBoard
def ZeroCutter(GM, GameBoard):
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
#All Possible Moves Amount for current GameBoard, np.sum(Ones_Counter(GameBoard))
def Scenarios(GM, GameBoard):
	it = 0
	ScenarioTable = []
	for p in range(0, np.sum(Ones_Counter(GameBoard))):
		ScenarioTable.append(copy.copy(GameBoard))	

	for i in GM:
		for j in i:
			for k in j:
				ScenarioTable[it][k[0]][k[1]] = 0		
			it += 1
	return(ScenarioTable)

#Algorithm Positions Generator 
def PGenerator(GameBoard):
	#Algorithm Starting Positions
	Positions = []
	
	for i in range(0,GameBoard.shape[0]):
		for j in range(0,GameBoard.shape[0]):
			if(GameBoard[i][j] == 1):
				Positions.append((i,j))
	return(Positions)

#Scenarios function Shortcut
def shortSC(GameBoard):
	return(Scenarios(ZeroCutter(GameMoves(PGenerator(GameBoard)), GameBoard), GameBoard))


#___________________________________________________________________________
#---------------------------------------------------------------------------
#___________________________________________________________________________


n = 4
GameBoard = CreateGameBoard(n)

#Way to get scenarios
#GameBoard -> PGenerator -> GameMoves -> Zerocutter -> Scenarios
#ShowMoves(Scenarios(ZeroCutter(GameMoves(PGenerator(GameBoard)), GameBoard), GameBoard))
