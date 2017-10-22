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

#Algorithm Starting Positions
Starting_Positions = []

#GameBoard creation
GameBoard = np.array([[1]*n]*n)

#Algorithm Starting Positions Generator 
for i in range(0,n):
	for j in range(0,n):
		Starting_Positions.append((i,j))

#All Possible Moves Amount for current GameBoard
PMA = np.sum(Ones_Counter(GameBoard))
