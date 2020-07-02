sudoku = [
        [0,0,0,0,0,0,2,0,0],
        [0,8,0,0,0,7,0,9,0],
        [6,0,2,0,0,0,5,0,0],
        [0,7,0,0,6,0,0,0,0],
        [0,0,0,9,0,1,0,0,0],
        [0,0,0,0,2,0,0,4,1],
        [0,0,5,0,0,0,6,0,3],
        [0,9,0,4,0,0,0,7,0],
        [0,0,6,0,0,0,0,0,0]
    ]

def possible(sudoku,r,c,n):
    for i in range(9):
        if sudoku[i][c]==n:
            return False
    for j in range(9):
        if sudoku[r][j]==n:
            return False
    x ,y = (r//3)*3 , (c//3)*3
    for k in range(3):
        for l in range(3):
            if sudoku[x+k][y+l]==n:
                return False
    return True
    
def solve(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                for n in range(1,10):
                    if possible(sudoku,i,j,n):
                        sudoku[i][j]=n
                        solve(sudoku)
                        sudoku[i][j]=0
                return
    print(sudoku)
    
solve(sudoku)

