import re

# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

counted_bags = set(['shiny gold bag'])
bag_rules = {}

def count_bags(bag):
    bags = 1
    if bag_rules[bag] == []:
        return bags
    for sub_bag in bag_rules[bag]:
        bags += int(sub_bag[0]) * count_bags(sub_bag[2:])
    return(bags)

for line in in_data:
    m1 = re.findall(r'\w+ \w+ bag', line)
    m2 = re.findall(r'\d \w+ \w+ bag', line)
    if(m2):
        bag_rules[m1[0]] = m2
    else:
        bag_rules[m1[0]] = []

print(count_bags('shiny gold bag')-1)
