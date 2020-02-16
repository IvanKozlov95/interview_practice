def isValid(row, col, rows, cols):
    return row >= 0 and row < rows and col >= 0 and col < cols

def minHour(rows, cols, grid):
    minHours = -1
    q = [(r, c) for c in range(cols) for r in range(rows) if grid[r][c] == 1]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while q:
        newQ = []
        for (row, col) in q:
            for (dir1, dir2) in directions:
                nextRow, nextCol = row + dir1, col + dir2
                if isValid(nextRow, nextCol, rows, cols) and grid[nextRow][nextCol] == 0:
                    grid[nextRow][nextCol] = 1
                    newQ.append((nextRow, nextCol))
        q = newQ
        print(newQ)
        minHours += 1

    return minHours

grid = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
print(minHour(5, 5, grid))
