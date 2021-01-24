with open('input') as f:
    in_data = [int(line.rstrip()) for line in f]

for i in range(0, len(in_data)):
    for j in range(0, len(in_data)):
        if i != j:
            v1 = in_data[i]
            v2 = in_data[j]
            if v1 + v2 == 2020:
                print(v1*v2)
                exit(0)

