#name = input("Your name: ")
#print("Hello ", name)

l = []
l.append(6)
l.extend([1, 2, 3, 4])
l.insert(3, "kuku")

print(l)

# Tuple

tup = (12, 34, 67, 'sdf')
lis = [12, 34, 67, 'sdf']

print (tup.__sizeof__())
print (lis.__sizeof__())

print (tup)

# Dictionary

d = {
  "one": {
    "k1": 1,
    "k2": 2
  },
  "two": {
    "k1": 10,
    "k2": 20
  }
}

print (d)

d2 = {a : a ** 2 for a in range(7)}

print (d2)

# Set

frozSet = frozenset(tup)

print (frozSet.__sizeof__())

# Functions

def pow (a, n):
  return a ** n


def out(a):
  def inside(b):
    return a + b
  return inside

k = out(100)
print (k(200))

lam = lambda *arg: sum(arg)

print (lam (1, 2, 3, "e", 5))