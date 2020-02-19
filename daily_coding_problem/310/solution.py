nibble_lookup_table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

def get_bits_number(n):
  bits = 0
  while n:
    nibble = n & 0xf
    bits += nibble_lookup_table[nibble]
    n = n >> 4
  return bits

def solution(N):
  total_bits = 0
  for i in range(N + 1):
    total_bits += get_bits_number(i)
  return total_bits


testcase1 = {
  'input': {
    'N': 31,
  },
  'expected': 80,
}
testcases = [testcase1]
