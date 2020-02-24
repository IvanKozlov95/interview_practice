def solution(str_time):
  hours, minutes = map(int, str_time.split(':'))
  hours %= 12
  minutes %= 60
  h_angle = 30 * hours + 0.5 * minutes
  m_angle = 6 * minutes
  return abs(h_angle - m_angle)

EQUALITY_TOLERANCE = 1.5

def bonus():
  for i in range(12):
    for j in range(60):
      time = '%02d:%02d' % (i, j)
      angle = solution(time)
      if angle <= EQUALITY_TOLERANCE:
        print('{} - {}'.format(time, angle))

bonus()

testcase1 = {
  'input': {
    'str_time': '12:20',
  },
  'expected': 110,
}
testcase2 = {
  'input': {
    'str_time': '12:00',
  },
  'expected': 0,
}
testcases = [testcase1, testcase2]
