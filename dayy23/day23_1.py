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


triple_pairs = []
for i in range(len(connections)):
    keys_list = list(connections.keys())
    key = keys_list[i]
    values = list(set(connections[key]))
    
    for v in values:
        for j in keys_list[i+1:]:
            if v in connections[j] and j in values:
                if any(set(triple) == {key, v, j} for triple in triple_pairs):
                    continue
                else:
                    if key[0] == 't' or v[0] == 't' or j[0] == 't':
                        triple_pairs.append((key, v, j))
                    
print(len(triple_pairs))