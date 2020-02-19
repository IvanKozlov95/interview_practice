import math

def shift(seq, n):
  return seq[n:]+seq[:n]

def is_there_space_to_move(filled):
  return filled[-1] == 0

def calculate_cost(filled, row):
  cost = 0
  filled_copy = filled[:]

  for idx, pos in enumerate(row):
    if pos == 1:
      if filled_copy[idx] == 1:
        filled_copy[idx] = 0
      else:
        one_idx = filled_copy.index(1)
        cost += abs(one_idx - idx)
        filled_copy[one_idx] = 0

  return cost

def solution(row, M, N):
  lowest_cost = math.inf
  filled = [1 for _ in range(M)] + [0 for _ in range(N - M)]
  while True:
    current_cost = calculate_cost(row, filled)
    if current_cost < lowest_cost:
      lowest_cost = current_cost
    if is_there_space_to_move(filled):
      filled = shift(filled, -1)
    else:
      break
  return lowest_cost

testcase1 = {
  'input': {
    'row': [0, 1, 1, 0, 1, 0, 0, 0, 1],
    'M': 4, 'N': 9,
  },
  'expected': 5.
}
testcase2 = {
  'input': {
    'row': [0, 1, 0],
    'M': 1, 'N': 3,
  },
  'expected': 0.
}

testcases = [testcase1, testcase2]