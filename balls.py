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

#Permutations Generator
def CrossCombine(St_Pos_List):
	#Knot positions	
	Pos_Moves = [St_Pos_List]
	Comb_Vec = [Pos_Moves]
	print("CV: ",Comb_Vec)
	#Vertical
	for i in range(St_Pos_List[0]+1, n):
		Pos_Moves.append([i, St_Pos_List[1]])
		print("PM: ",Pos_Moves)
		#Comb_Vec.extend([Pos_Moves])
		#print("CV: ",Comb_Vec)
	#Horizontal
	Pos_Moves = [St_Pos_List]
	for j in range(St_Pos_List[1]+1, n):
		Pos_Moves.append([St_Pos_List[0],j])
		print("PM: ",Pos_Moves)
		#Comb_Vec.extend([Pos_Moves])
		#print("CV: ",Comb_Vec)
	#Return Cross elements from Knot position
	return(Pos_Moves)
	#return(Pos_Moves)

#Algorithm Starting Positions
Starting_Positions = []

#GameBoard creation
GameBoard = np.array([[1]*n]*n)

#Algorithm Starting Positions Generator 
for i in range(0,n):
	for j in range(0,n):
		Starting_Positions.append([i,j])

#All Possible Moves Amount for current GameBoard
PMA = np.sum(Ones_Counter(GameBoard))

