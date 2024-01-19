import math
def calc_gcd(x, y):
  while y:
      x, y = y, x % y
  return x

def calc_lcm(n1, n2):
  return n1 * n2 // math.gcd(n1, n2)

def gcdOfList(l):
  res = []
  for index, item in enumerate(l):
    res[index] = calc_lcm(res[, )

l = [36, 25]

print()

#print(math.lcm(n, m))
#print(math.gcd(n, m))