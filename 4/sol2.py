import re

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def eval_hgt(hgt):
    if (hgt.endswith("cm")):
        return 150 <= int(hgt[:-2]) <= 193
    elif (hgt.endswith("in")):
        return 59 <= int(hgt[:-2]) <= 76
    else:
        return False

field_contraints = {
    "byr": lambda x: 2002 >= int(x) >= 1920,
    "iyr": lambda x: 2020 >= int(x) >= 2010,
    "eyr": lambda x: 2030 >= int(x) >= 2020,
    "hgt": lambda x: eval_hgt(x),
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x) is not None,
    "ecl": lambda x: x in eye_colors,
    "pid": lambda x: re.match("^\d{9}$", x) is not None,
    "cid": lambda x: True,
}

with open('input') as f:
    in_data = [line.rstrip() for line in f]

passports_valid = 0

current_passport = []
i=0
while i < len(in_data):
    line = in_data[i]

    # Read fields until newline
    if line != "":
        m = re.findall(r'\w+:[^\s]*', line)
        current_passport += m
        i+=1
        continue

    # Convert to dict
    passport_as_dict = {}
    for field in current_passport:
        split = field.split(':')
        key = split[0]
        val = split[1]
        passport_as_dict[key] = val

    #print(passport_as_dict)

    valid = True;
    for field in passport_as_dict.keys():
        if field == "hcl":
            if not field_contraints[field](passport_as_dict[field]):
                valid = False
                i+=1
                break
            else:
                print(field + ", " + passport_as_dict[field])
                print(field_contraints[field](passport_as_dict[field]))

    # Field present check
    if valid:
        for field in valid_fields:
            if field not in passport_as_dict.keys():
                valid = False
                current_passport = []
                i+=1
                break
    if valid:
        passports_valid+=1
        current_passport = []
        i+=1

print(passports_valid)
