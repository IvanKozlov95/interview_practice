class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def remove_consecutive_zeroes(self):
    _sum = 0
    node = Node(0, self)
    head = node
    nodes_dict = {}

    while node:
      _sum += node.val
      if _sum in nodes_dict:
        nodes_dict[_sum].next = node.next
      else:
        nodes_dict[_sum] = node
      node = node.next
    
    return head.next

  @staticmethod
  def to_py_list(node):
    if node is None or node.val is None:
      return []
    return [node.val] + Node.to_py_list(node.next)

  @staticmethod
  def from_py_list(values = []):
    if len(values) == 0:
      return None
    head = Node(values[0])
    current = head

    for value in values[1:]:
      current.next = Node(value)
      current = current.next
    return head

  def __str__(self):
    str_val = str(self.val)
    if self.next:
      str_val += ' -> {}'.format(str(self.next))
    return str_val

def solution(py_list):
  linked_list = Node.from_py_list(py_list)
  return Node.to_py_list(linked_list.remove_consecutive_zeroes())

testcase1 = {
  'input': {
    'py_list': [3, 4, -7, 5, -6, 6],
  },
  'expected': [5],
}
testcase2 = {
  'input': {
    'py_list': [3, 4, -7, -6, 6],
  },
  'expected': [],
}
testcase3 = {
  'input': {
    'py_list': [3, 4, -7, 5, -6, 6, -5],
  },
  'expected': [],
}
testcase4 = {
  'input': {
    'py_list': [-5, 5, -6, 6],
  },
  'expected': [],
}

testcases = [testcase1, testcase2, testcase3, testcase4]
