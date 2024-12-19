import re



with open("dayy19/input.txt") as f:
    inp = f.read().splitlines()
    towels = [ x.strip() for x in inp[0].split(',') ]
    patterns = inp[inp.index('')+1:]
    
    
total = 0


for p in patterns:
    # regex ^ to match from the start of the string, $ patters must cover full string
    regx_patrn = r"^(" + r"|".join(towels) + r")+$"
    if re.fullmatch(regx_patrn, p):
        total += 1
        
print(total)