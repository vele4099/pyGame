data_set = {2, 3, 3, 8, 14, 8, 23, 14}
#must be immutable
#un-hashable a way to figure out a signiture for objects in memory (memory allocations like binary)
functions = dir(data_set)

for i in functions:
    if '_' not in i: 
        print(i)


data_set.remove(3)
print(data_set)
data_set.add(34)
print(data_set)

data_set2 = {12, 18, 16, 15, 8, 22}
print(data_set.intersection(data_set2))

print(data_set.union(data_set2))

print(data_set.difference(data_set2))
data_set.remove(8)

print(data_set.isdisjoint(data_set2))


print(data_set.issubset(data_set2))