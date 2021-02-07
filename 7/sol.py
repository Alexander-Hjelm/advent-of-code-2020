import re

# Data processing
with open('input') as f:
    in_data = [line.rstrip() for line in f]

counted_bags = set(['shiny gold bag'])
tentative_bag_rules = []

for line in in_data:
    m = re.findall(r'\w+ \w+ bag', line)
    tentative_bag_rules.append(m)

bag_added = True
while bag_added:
    bag_added = False
    for bag_rule in tentative_bag_rules:
        found_bags_to_count = []
        for bag in counted_bags:
            if bag in bag_rule[1:] and bag_rule[0] not in counted_bags:
                found_bags_to_count.append(bag_rule[0])
                bag_added = True
        counted_bags = counted_bags.union(set(found_bags_to_count))

print(len(counted_bags)-1)
