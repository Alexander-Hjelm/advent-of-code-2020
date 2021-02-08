# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

summed = 26134589

for i in range(0, len(in_data)):
    s=0
    j=i
    traversed_set = []
    while s < summed:
        traversed_set.append(int(in_data[j]))
        s += int(in_data[j])
        if(s==summed):
            print(min(traversed_set) + max(traversed_set))
            exit(0)
        j+=1
