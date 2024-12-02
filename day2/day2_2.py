with open("input.txt", "r") as f:
    inp = f.readlines()
    
inp = [x.strip().split(" ") for x in inp]
inp = [list(map(int, x)) for x in inp]

def is_increasing(report):
    for i in range(0, len(report)-1):
        if (report[i] >= report[i+1]):
            return False
    return True

def is_decreasing(report):
    for i in range(0, len(report)-1):
        if (report[i] <= report[i+1]):
            return False
    return True

def valid_report(report):
    for i in range(0, len(report)-1):
        if 1 < abs(report[i] - report[i+1]) > 3:
            return False
    return True

def check_bad_level(report):
    for i in range(0, len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if (is_increasing(new_report) or is_decreasing(new_report)) and valid_report(new_report):
            return True
    return False
        
        

total = 0

for rep in inp:
    if (is_increasing(rep) or is_decreasing(rep)) and valid_report(rep):
        total += 1
        continue
    if check_bad_level(rep):
        total += 1
        continue


print(total)