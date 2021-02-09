# Data processing
with open('input') as f:
    in_data = [int(line.rstrip()) for line in f]

"""
def find_paths(adapters, joltage):
   # print(joltage)
   # print(adapters)
    if(len(adapters) == 1):
        return 1
    else:
        paths=0
        for i in range(0, len(adapters)):
            if abs(joltage-adapters[i]) <= 3:
                print("===")
                print(joltage)
                print(adapters[i])
                paths+=find_paths(list(set(adapters)-set([adapters[i]])), -joltage+adapters[i])
        #exit(0)
        return paths

in_data.append(max(in_data)+3)    
print(find_paths(in_data, 0))

"""

in_data.append(max(in_data)+3)
in_data.append(0)
in_data.sort()

diff_1 = 0
diff_3 = 0

for i in range(1, len(in_data)):
    diff = in_data[i] - in_data[i-1]
    if diff == 1:
        diff_1+=1
    elif diff == 3:
        diff_3+=1

print(diff_1*(diff_3))
