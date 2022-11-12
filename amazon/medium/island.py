# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

def visit(matrix, i, j):

  directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
  for direction in directions:
    x, y = direction[0] + i, direction[1] + j

    if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] == 1:
      matrix[x][y] = 2
      visit(matrix, x, y)


def islands(matrix):
  counter = 0

  for i in range( len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 1:
        matrix[i][j] = 2
        visit(matrix, i, j)
        counter += 1

  return counter


print(islands(
[
[1, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 0, 0, 1],
[1, 1, 0, 0, 1]
]

))