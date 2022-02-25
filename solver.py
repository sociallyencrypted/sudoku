def validateNum(grid, row, col, num):
    """Returns if a specific number is a valid guess for the given row and column

    :param grid: the grid for the sudoku
    :type grid: list
    :param row: row number
    :type row: int
    :param col: column number
    :type col: int
    :param num: guess number to be checked
    :type num: int

    :rtype: bool
    :return: True or False based on the validity of the number
    """
    for i in range(9):
        if grid[row][i] == num:
            return False
    for i in range(9):
        if grid[i][col] == num:
            return False
    for i in range(3):
        for j in range(3):
            if grid[i + row - (row % 3)][j + col - (col % 3)] == num:
                return False
    return True


def validateGrid(grid):
    """Returns if the input grid is valid

    :param grid: the grid for the sudoku
    :type grid: list

    :rtype: bool
    :return: True or False based on the validity of the grid
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                num = grid[i][j]
                grid[i][j] = 0  # Setting grid position to 0 temporarily
                if not validateNum(grid, i, j, num):
                    grid[i][j] = num
                    return False
                grid[i][j] = num
    return True


def gridPrint(grid):
    """Prints a given sudoku grid

    :param grid: the grid to be printed
    :type grid: list
    """
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


def storeRow(line):
    """Takes a line and converts it itno a row

    :param line: the line entered by the user
    :type grid: str
    """
    rowList = [int(x) for x in line.split()]
    return rowList


def solve(grid, row, col):
    """Returns if a grid is solveable, changing the grid in situ.

    :param grid: the grid for the sudoku
    :type grid: list
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

    if grid[row][col] > 0:
        return solve(grid, row + 1, col)

    for i in range(1, 10):
        if validateNum(grid, row, col, i):
            grid[row][col] = i
            if solve(grid, row + 1, col):
                return True
        grid[row][col] = 0
    return False


while True:
    grid = []
    print(
        "Format of entering rows: Space Seperaretd Numbers, replacing unknowns with 0. For eg. 3 0 1 0 0 0 4 0 5"
    )
    for i in range(9):
        ln = input("Enter row " + str(i) + ": ")
        grid.append(storeRow(ln))
    if validateGrid(grid):
        if solve(grid, 0, 0):
            gridPrint(grid)
        else:
            print("Unsolveable :(")
        choice = input("Want to solve another one (y/n): ")
        if choice == "n":
            break
    else:
        print(
            "Invalid grid! Some of the numbers are repeated in a row, column or 3x3 box. Please check your input and try again."
        )
