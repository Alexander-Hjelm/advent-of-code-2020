import re

# Data processing
with open('input') as f:
    in_data = f.read().split("\n\n")

for i in range(0,len(in_data)):
    in_data[i] = in_data[i].replace('\n', '')

# Count set lengths
res = 0
for line in in_data:
    res += len(set(line))

print(res)

print(set('aaaabbcdddee'))
print(set([1, 1, 2, 3, 4, 4, 5]))
