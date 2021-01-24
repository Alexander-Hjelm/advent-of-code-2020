with open('input') as f:
    in_data = [line.rstrip() for line in f]

w=len(in_data[0])
tree_count_mul=1
for p in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    j=0
    tree_count=0
    for i in range(p[1], len(in_data), p[1]):
        line = in_data[i]
        j=(j+p[0])%w
        if line[j] == '#':
            tree_count+=1
    tree_count_mul*=tree_count
    print(tree_count)
print(tree_count_mul)
