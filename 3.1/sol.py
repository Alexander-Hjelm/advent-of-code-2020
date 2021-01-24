with open('input') as f:
    in_data = [line.rstrip() for line in f]

j=0
w=len(in_data[0])
tree_count=0
for i in range(1, len(in_data)):
    line = in_data[i]
    j=(j+3)%w
    if line[j] == '#':
        tree_count+=1
print(tree_count)
