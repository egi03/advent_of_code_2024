from functools import cache

def arrange_towels():
    global pattern
    total_matches = 0
    for pattern in patterns:
        match_pattern.cache_clear() 
        matches = match_pattern(0)
        total_matches += matches
    return total_matches

@cache
def match_pattern(pos):
    matches = 0
    for t in towels.get(pattern[pos:pos+1],''):
        new_pos = pos + len(t)
        if pattern[pos:new_pos] == t:
            if new_pos == len(pattern):
                matches += 1
            else:
                matches += match_pattern(new_pos)     
    return matches


with open("dayy19/input.txt") as f:
    input = f.read().splitlines()

towels = {}
patterns = []

for l, line in enumerate(input):
    if l == 0:
        unsorted_towels = line.split(', ')
    elif l == 1:
        pass
    else:
        patterns.append(line)

for unsorted in unsorted_towels:
    if unsorted[0] not in towels:
        towels[unsorted[0]] = []
    towels[unsorted[0]].append(unsorted)
    
    
print(arrange_towels())