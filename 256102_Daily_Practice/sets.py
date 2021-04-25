a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))