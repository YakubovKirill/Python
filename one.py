import math
import time
import os
import mod
from Person import Person

print(os.getenv("TMP"))

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

#lam = lambda *arg: sum(arg)
#print (lam (1, 2, 3, "e", 5))

# Try catch

x = 2
y = 4

try: 
  res = x / y
  print (res)
except Exception:
  print('err')
finally:
  print ("Okey")

# Files

f = open ('text.txt', 'r+')
#f.read ()
for line in f:
  print (line)
#print (f)
f.close ()

# Modules

print (math.pi)

# Classes

kirill = Person()
kirill.set("Kirill", 22)

print(kirill.getName())
print(kirill.getAge())