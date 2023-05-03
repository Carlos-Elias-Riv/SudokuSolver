class Solver:
    def __init__(self, sudoku: list):
        self.sudoku = sudoku
        self.solved = False
        self.blankspaces = {} # (ren0, col0): False 
        self.sets = {0:set(), 1: set(), 2:set(), 3:set(), 4:set(), 5:set(), 6:set(), 7:set(), 8:set() } 
    
    def solve(self):
        self.obtainBlanksandSets()
        primerspace = self.nextBlankSpace()
        if primerspace is not None:
            self.solveRec(primerspace)
        
    def printSetsAndBlankSpaces(self):
        self.obtainBlanksandSets()
        print(f'Los sets son: \n{self.sets}')
        print(f'Los blankspaces son: \n{self.blankspaces}')

    def nextBlankSpace(self):
        lista = list(self.blankspaces)
        solved_list = [self.blankspaces[key] for key in self.blankspaces]
        if all(solved_list):
            return None
        else:
            for elem in lista:
                if not self.blankspaces[elem]:
                    return elem


    def solveRec(self, space):
        if space is None:
            return True
        solved_list = [self.blankspaces[key] for key in self.blankspaces]

        # Veo si ya lo resolví
        if all(solved_list):
            return True

        # Si no esta resuleto, entonces empiezo a probar los espacios faltantes
        solved = False

        
        i = 1
        columna = [self.sudoku[ren][space[1]] for ren in range(9)]
        setno = space[1]//3 + (space[0]//3)*3
        while i < 10 and not solved:
            # Checamos por renglón, checamos por cuadro, falta checar por columna
            if i not in self.sudoku[space[0]] and i not in self.sets[setno] and i not in columna: 
                # Pongo el numero en el sudoku
                self.sudoku[space[0]][space[1]] = i
                # Pongo que ya resolví el espacio que me faltaba
                self.blankspaces[space] = True
                # Agrego al set el numero, al set que le corresponde
                self.sets[setno].add(i)
                # Intento resolverlo a partir de lo último que hice con un nuevoblankspace
                newspace = self.nextBlankSpace()
                solved = self.solveRec(newspace)
                # Si no se pudo solucionar con ese numero
                if not solved: 
                    # reinicio el sudoku
                    self.sudoku[space[0]][space[1]] = 0
                    # no he resuelto ese espacio
                    self.blankspaces[space] = False
                    # quito el valor del set
                    self.sets[setno].discard(i)
            i += 1

        if i >= 10 and not solved:
            return False
        else: 
            return solved

        



    def obtainBlanksandSets(self):
        for ren in range(len(self.sudoku)):
            for col in range(len(self.sudoku[ren])):
                if self.sudoku[ren][col] == 0:
                    self.blankspaces[(ren, col)] = False
                else:
                    setno = col//3 + (ren//3)*3
                    self.sets[setno].add(self.sudoku[ren][col])

    def printSudoku(self):
        for row in self.sudoku:
            for elem in row:
                print(elem, end = " ")

            print("\n")