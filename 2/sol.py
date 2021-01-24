import re

with open('input') as f:
    in_data = [line.rstrip() for line in f]

pws_valid = 0

for i in range(0, len(in_data)):
    line = in_data[i]
    m = re.match(r'(?P<i1>\d+)-(?P<i2>\d+) (?P<c>\w): (?P<w>\w+)', line)
    i1 = int(m.group('i1'))
    i2 = int(m.group('i2'))
    c = m.group('c')
    w = m.group('w')

    count = w.count(c)
    if count >= i1 and count <= i2:
        pws_valid+=1

print(pws_valid)
