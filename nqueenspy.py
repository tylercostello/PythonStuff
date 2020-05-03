#numqueens=int(input("How many queens? "))
numqueens=2
board=[]
for x in range(0,numqueens*numqueens):
    board.append(0)
length=len(board)
#empty board created
for x in range(0,numqueens):
    board[x]=1
#starting queens
def generateall(board):
    #print(board)
    temp=board[length-1]
    for x in range(0,length-1):
        x=length-1-x
        
print(generateall(board))
