sudoku = [
    [0,0,0,0,0,8,3,2,0],
    [0,6,0,0,0,0,0,0,0],
    [3,4,0,2,0,0,5,0,0],
    [0,0,6,3,0,0,0,0,0],
    [1,3,0,0,0,9,0,0,4],
    [0,0,8,0,0,0,1,0,0],
    [0,0,0,0,7,0,0,0,9],
    [0,0,1,0,0,0,0,0,0],
    [5,2,0,8,0,0,4,0,0]
]
# for row in sudoku:
#     for elem in row:
#         print(elem, end=" ")
#     print("\n")


from Solver import Solver
solucionador = Solver(sudoku)
#solucionador.printSets()
solucionador.solve()
solucionador.printSudoku()