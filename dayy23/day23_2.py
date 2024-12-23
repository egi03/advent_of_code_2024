data = []

with open("dayy23/input.txt") as f:
    for x in f.read().splitlines():
        data.append(x.split("-"))        

# node: all_connected_nodes    
connections = {}

for pair in data:
    x, y = pair
    if x in connections.keys():
        connections[x].append(y)
    else:
        connections[x] = [y]
    
    if y in connections.keys():
        connections[y].append(x)
    else:
        connections[y] = [x]


all_sets = set()

def get_connected(x, conns):
    new_set = tuple(sorted(conns))
    if new_set in all_sets:
        return
    all_sets.add(new_set)
    candidates = connections[x]
    for c in candidates:
        if c in conns:
            continue
        # check if candidate in connected to everything in conns list
        if all(cc in connections[c] for cc in conns):
            temp = set(conns)
            temp.add(c)
            get_connected(c, temp)
            
                    
for x in connections:
    get_connected(x, {x})
    
print(",".join(max(all_sets, key=len)))