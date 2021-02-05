import re

def bsp(pattern, u_token):
    upper=2**len(pattern)-1
    lower=0
    for c in pattern[:len(pattern)]:
        if c == u_token:
            upper = (lower+upper)/2-0.5
        else:
            lower += (upper-lower)/2+0.5
    return lower

with open('input') as f:
    in_data = [line.rstrip() for line in f]

highest = 0

for line in in_data:
    row = bsp(line[0:7], 'F')
    seat = bsp(line[7:10], 'L')

    seat_id = row*8+seat
    if seat_id > highest:
        highest = seat_id
print(highest)

