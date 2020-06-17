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