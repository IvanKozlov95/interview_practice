from collections.abc import Iterable

def is_square(matrix):
  rows = len(matrix)
  for row in matrix:
    if len(row) != rows:
      return False
  return True

def check_diagonal(idx, val, matrix):
  for row in matrix:
    if len(row) <= idx:
      break
    if val != row[idx]:
      return False
    idx += 1
  return True

def solution(matrix):
  if matrix is None:
    return False

  for row in matrix:
    if not isinstance(row, Iterable):
      return False

  for (row_idx, row) in enumerate(matrix):
    for (col_idx, el) in enumerate(row):
      if not check_diagonal(col_idx, el, matrix[row_idx:]):
        return False
      if row_idx != 0:
        break
  return True

matrix1 = [[1]]
matrix2 = [[1, 2, 3]]
matrix3 = [
  [1, 2, 3],
  [2, 1, 2],
  [5, 1, 1],
]
matrix4 = [1]
matrix5 = [
  [1, 2, 3, 4, 8],
  [5, 1, 2, 3, 4],
  [4, 5, 1, 2, 3],
  [7, 4, 5, 1, 2],
]

testcase1 = {
  'input': {
    'matrix': matrix1,
  },
  'expected': True,
}
testcase2 = {
  'input': {
    'matrix': matrix2,
  },
  'expected': True,
}
testcase3 = {
  'input': {
    'matrix': matrix3,
  },
  'expected': False,
}
testcase4 = {
  'input': {
    'matrix': matrix4,
  },
  'expected': False,
}
testcase5 = {
  'input': {
    'matrix': matrix5,
  },
  'expected': True,
}
testcases = [testcase1, testcase2, testcase3, testcase4, testcase5]
