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

#Algorithm Starting Positions Generator 
def SPGenerator(n):
	#Algorithm Starting Positions
	Starting_Positions = []
	
	for i in range(0,n):
		for j in range(0,n):
			Starting_Positions.append((i,j))
	return(Starting_Positions)

n=4
#GameBoard creation
GameBoard = np.array([[1]*n]*n)

#Algorithm Starting Positions
Starting_Positions = SPGenerator(n)

#All Possible Moves Amount for current GameBoard
PMA = np.sum(Ones_Counter(GameBoard))

#Ones Counter List (V+H elements)
OC_List = Ones_Counter(GameBoard)
