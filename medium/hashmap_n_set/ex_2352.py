from typing import List

# 2352 Equal Row and Column Pairs
def equalPairs(grid: List[List[int]]) -> int:
        counter = {}
        for r, i in enumerate(grid):
            row = tuple(i)
            if row in counter:
                counter[row] += 1
            else:
                counter[row] = 1

        res = 0
        for j in range(len(grid)):
            column = []
            for i in range(len(grid)):
                column.append(grid[i][j])
            column = tuple(column)
            if column in counter:
                res += counter[column]
        return res

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))

# Array, Hash Table, Matrix, Simulation