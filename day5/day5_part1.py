def check_update(update, rules):
    first_rules_args = [rule[0] for rule in rules]
    
    for i, x in enumerate(update):
        if x not in first_rules_args:
            continue
        
        for rule in rules:
            if rule[0] == x and rule[1] in update:
                if update.index(x) > update.index(rule[1]):
                    return 0
    return update[int(len(update)/2)]

with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]
    
ind_to_split = inp.index('')
rules = [list(map(int, x.split('|'))) for x in inp[0:ind_to_split]]
updates = [list(map(int, x.split(','))) for x in inp[ind_to_split+1:]]

print(sum([check_update(x, rules) for x in updates]))