import traceback


class Grid:
    """represents a two-dimensional, positional Grid
    implemented through nested lists"""

    def __init__(self):
        """Initialise grid"""
        self.grid = []

    def storeRow(self, line):
        """Takes a line and converts it into a row"""
        rowList = [int(x) for x in line.split()]
        return rowList

    def addrow(self, row):
        row = self.storeRow(row)
        if self.validateRow(row):
            self.grid.append(row)
            return True
        else:
            print("Invalid row, try again!")
            return False

    def __len__(self):
        """Returns number of rows
        :rtype: int
        :return: number of rows
        """
        return len(self.grid)

    def __getitem__(self, index):
        """Gets a certain index of the sudoku grid
        :param index: index to be returned
        :type index: int
        :rtype: list/int
        :return: item at given index of the grid"""
        return self.grid[index]

    def __str__(self):
        """Defines the print() and str() value of the grid
        :rtype: str
        :return: Space seperated values and newline seperated rows
        """
        string = ""
        for i in range(9):
            for j in range(9):
                string += str(self[i][j]) + " "
            string += "\n"
        return string

    def validateGrid(self):
        """Returns if the input grid is valid
        :rtype: bool
        :return: True or False based on the validity of the grid
        """
        for i in range(9):
            for j in range(9):
                if self[i][j] != 0:
                    num = self[i][j]
                    self[i][j] = 0  # Setting grid position to 0 temporarily
                    if not self.validateNum(self.grid, i, j, num):
                        self[i][j] = num
                        return False
                    self[i][j] = num
        return True

    def validateNum(self, grid, row, col, num, nr=9, cr=9, gr=3):
        """Returns if a specific number is a valid guess for the given row and column
        :param grid: the grid for the sudoku
        :type grid: list
        :param row: row number
        :type row: int
        :param col: column number
        :type col: int
        :param num: guess number to be checked
        :type num: int
        :param nr: number of rows
        :type nr: int
        :param cr: number of columns
        :type cr: int
        :param gr: subgrid size
        :type gr: int
        :rtype: bool
        :return: True or False based on the validity of the number
        """
        for i in range(nr):
            if grid[row][i] == num:
                return False
        for i in range(cr):
            if grid[i][col] == num:
                return False
        for i in range(gr):
            for j in range(gr):
                if grid[i + row - (row % 3)][j + col - (col % 3)] == num:
                    return False
        return True

    def validateRow(self, row):
        """Returns if an input row is valid
        :param row: row
        :type row: list
        :rtype: bool
        :return: True or False based on the validity of the row
        """
        for i in range(9):
            if row[i] != 0:
                num = row[i]
                row[i] = 0  # Setting grid position to 0 temporarily
                rows = [row]
                if not self.validateNum(rows, 0, 0, num, 9, 0, 0):
                    row[i] = num
                    print(i, row)
                    return False
                row[i] = num
        return True

    def solve(self, row=0, col=0):
        """Returns if a grid is solveable, changing the grid in situ.
        :param row: row number
        :type row: int
        :param col: column number
        :type col: int
        :rtype: bool
        :return: True or False based on whether the sudoku grid is solveable
        """
        if col == 8 and row == 9:
            return True

        if row == 9:
            col += 1
            row = 0

        if self[row][col] > 0:
            return self.solve(row + 1, col)

        for i in range(1, 10):
            if self.validateNum(self.grid, row, col, i):
                self[row][col] = i
                if self.solve(row + 1, col):
                    return True
            self[row][col] = 0
        return False


while True:
    # grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9],
    # ] # Sample Grid
    print(
        "Format of entering rows: Space Seperaretd Numbers, replacing unknowns with 0. For eg. 3 0 1 0 0 0 4 0 5"
    )
    sudoku = Grid()
    for i in range(9):
        while True:
            try:
                ln = input("Enter row " + str(i) + ": ")
                # ln = " ".join([str(x) for x in grid[i]])
                if sudoku.addrow(ln):
                    break
            except KeyboardInterrupt:
                exit()
                raise
            except:
                print("Invalid row, try again!")
                traceback.print_exc()

    if sudoku.validateGrid():
        if sudoku.solve():
            print(sudoku)
        else:
            print("Unsolveable :(")
        choice = input("Want to solve another one (y/n): ")
        if choice == "n":
            break
    else:
        print(
            "Invalid grid! Some of the numbers are repeated in a row, column or 3x3 box. Please check your input and try again."
        )
