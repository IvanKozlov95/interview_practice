def is_peak(arr, idx):
  return arr[idx - 1] < arr[idx] and arr[idx] > arr[idx + 1]

def find_peak(arr):
  _len = len(arr)
  if _len <= 2:
    return None

  mid = len(arr) // 2
  if is_peak(arr, mid):
    return arr[mid]
  left_peak = find_peak(arr[0:mid+1])
  if left_peak is not None:
    return left_peak
  return find_peak(arr[mid:_len])


solution = find_peak

testcase1 = {
  'input': {
    'arr': [1, 2, 0],
  },
  'expected': 2,
}
testcase2 = {
  'input': {
    'arr': [1, 2, 3, 4, 5, 8, 7, 9, 10, 0],
  },
  'expected': 8,
}
testcase3 = {
  'input': {
    'arr': [1, 2, 3, 4, 5, 6, 7, 9, 8, 0],
  },
  'expected': 9,
}
testcase4 = {
  'input': {
    'arr': [1, 9, 3, 4, 5],
  },
  'expected': 9,
}
testcases = [testcase1, testcase2, testcase3, testcase4]