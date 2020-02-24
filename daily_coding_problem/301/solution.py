class ApproxSet:
  def __init__(self):
    self.value = 0

  def add(self, value):
    self.value |= hash(value)

  def check(self, value):
    return bool(self.value & hash(value))

print(hash(123))
print(hash('ivan'))
aset = ApproxSet()
aset.add(1)
print(aset.check(1))
print(aset.check(2))
aset.add('ivan')
print(aset.check(2))
print(aset.check('ivn'))