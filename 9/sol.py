# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

for i in range(25, len(in_data)):
    pre_i = in_data[i-25:i]
    summed_pair_found = False
    for a in pre_i:
        for b in pre_i:
            if a != b:
                if int(a)+int(b) == int(in_data[i]):
                    summed_pair_found = True
    if not summed_pair_found:
        print(in_data[i])
        exit()
