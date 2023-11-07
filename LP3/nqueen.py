global N
N = 4
  
def printSolution(board): 
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print() 


def isSafe(board, row, col):
  
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
  
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True

def solveNQUtil(board, col):
    
    if col >= N:
        return True
  
    for i in range(N):
  
        if isSafe(board, i, col):
              
            board[i][col] = 1
            
            if solveNQUtil(board, col + 1) == True:
                return True
  
            board[i][col] = 0
  
    return False

def solveNQ():
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]
  
    if solveNQUtil(board, 0) == False:
        print ("Solution doesn't exist")
        return False
  
    printSolution(board)
    return True
  
# Driver Code
solveNQ()


## using backtracking.
## Backtracking : it is an algo technique for solving problems recursively by trying to build a solution incrementally , one piece at a time,
## removing those solutions that fails to satisfy the constraints of the problem at any point of time.

#time complexity: O(N!)  -> 
# space complexity: O(N) -> due to call stack
