import re
print(sum([ 1 for p in open("dayy19/input.txt").read().splitlines()[open("dayy19/input.txt").read().splitlines().index('')+1:] if re.fullmatch(r"^(" + r"|".join([ x.strip() for x in open("dayy19/input.txt").read().splitlines()[0].split(',') ]) + r")+$", p)]))