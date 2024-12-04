def check_up(list_ind, char_ind, inp):
    try:
        return inp[list_ind][char_ind+2] == 'M' and inp[list_ind+2][char_ind] == inp[list_ind+2][char_ind+2] =='S' and inp[list_ind+1][char_ind+1] == 'A'
    except IndexError:
        return False
    
def check_down(list_ind, char_ind, inp):
    try:
        return inp[list_ind][char_ind+2] == 'M' and inp[list_ind-2][char_ind] == inp[list_ind-2][char_ind+2] =='S' and inp[list_ind-1][char_ind+1] == 'A'
    except IndexError:
        return False

def check_right(list_ind, char_ind, inp):
    try:
        return inp[list_ind+2][char_ind] == 'M' and inp[list_ind][char_ind-2] == inp[list_ind+2][char_ind-2] =='S' and inp[list_ind+1][char_ind-1] == 'A'
    except IndexError:
        return False

def check_left(list_ind, char_ind, inp):
    try:
        return inp[list_ind+2][char_ind] == 'M' and inp[list_ind][char_ind+2] == inp[list_ind+2][char_ind+2] =='S' and inp[list_ind+1][char_ind+1] == 'A'
    except IndexError:
        return False



with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]
total = 0
for ind_l, lst in enumerate(inp):
    for ind_c, c in enumerate(lst):
        if c == 'M':
            total += sum([
                check_right(ind_l, ind_c, inp),
                check_left(ind_l, ind_c, inp),
                check_up(ind_l, ind_c, inp),
                check_down(ind_l, ind_c, inp),
            ])

print(total)