with open('input_jac.txt') as f:
    data = [d.strip() for d in f.readlines()]
    
from itertools import permutations
    
seating = []
for d in data:
    l = d.split(' ')
    person = l[0]
    neighbour = l[-1][:-1]
    if 'lose' in l:
        value = int(l[3]) * -1
    else:
        value = int(l[3])
    seating.append((sorted([person, neighbour]), value))
seating = sorted(seating)

names = set()
seating_map = dict()
for (a, b), (x, y) in zip(seating[::2], seating[1::2]):
    first, second = a
    names.add(first)
    names.add(second)
    seating_map[(first, second)] = b + y
    seating_map[(second, first)] = b + y
    
pt1 = 0
for p in permutations(names, 8):
    pairs = list(zip(p, p[1:]))
    pairs.append((p[0],p[-1]))
    total = sum([seating_map[pair] for pair in pairs])
    if total > pt1:
        pt1 = total
print(pt1)

for name in names:
    seating_map[('James', name)] = 0
    seating_map[(name, 'James')] = 0
names.add('James')
    
pt2 = 0
total = 0
for p in permutations(names, 9):
    pairs = list(zip(p, p[1:]))
    pairs.append((p[0],p[-1]))
    total = sum([seating_map[pair] for pair in pairs])
    if total > pt2:
        pt2 = total
print(pt2)


