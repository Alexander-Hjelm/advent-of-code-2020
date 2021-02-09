import re

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open('input') as f:
    in_data = [line.rstrip() for line in f]

passports_valid = 0

current_passport = []
i=0
while i < len(in_data):
    line = in_data[i]

    if line != "":
        m = re.findall(r'\w+:', line)
        current_passport += m
        i+=1
        continue

    valid = True;
    for field in valid_fields:
        if field+':' not in current_passport:
            valid = False
            current_passport = []
            i+=1
            break
    if valid:
        passports_valid+=1
        current_passport = []
        i+=1

print(passports_valid)
