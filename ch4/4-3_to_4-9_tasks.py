# 4-3

for value in range(1, 21):
    print(value)

# 4-4

million = []

for millions in range(1, 1000001):
    million.append(millions)
    print(millions)

#4-5

print(min(million))
print(max(million))
print(sum(million))

# 4-6

odd = []
for odds in range(1, 20, 2):
    odd.append(odds)
    print(odds)

print(odd)

# 4-7

threes = []
for three in range(3, 31, 3):
    threes.append(three)
    print(three)

# 4-8

cubes = []

for cube in range(1, 11):
    cubes.append(cube**3)

print(cubes)
# 4-9

lcubes = [lcube**3 for lcube in range(1,11)]
print(lcubes)
