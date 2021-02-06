import re

# Data processing
with open('input') as f:
    in_data = f.read().split("\n\n")

for i in range(0,len(in_data)):
    in_data[i] = in_data[i].split('\n')

# Count intersection lengths
res = 0
for line in in_data:
    sets = []
    for answer in line:
        if answer != '':
            sets.append(set(answer))
    res += len(set.intersection(*[x for x in sets]))

# To document:
# set.intersection
# set
