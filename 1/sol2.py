with open('input') as f:
    in_data = [int(line.rstrip()) for line in f]

for i in range(0, len(in_data)):
    for j in range(0, len(in_data)):
        if i != j:
            for k in range(0, len(in_data)):
                if k != i and k != j:
                    v1 = in_data[i]
                    v2 = in_data[j]
                    v3 = in_data[k]
                    if v1 + v2 + v3 == 2020:
                        print(v1*v2*v3)
                        exit(0)

