# Data processing
with open('input') as f:
    in_data = [int(line.rstrip()) for line in f]

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
