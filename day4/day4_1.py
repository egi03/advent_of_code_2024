def check_right(list_ind, char_ind, text):
    if char_ind + 4 > len(text[list_ind]):
        return False
    return text[list_ind][char_ind:char_ind+4] == "XMAS"

def check_left(list_ind, char_ind, text):
    if char_ind - 3 < 0:
        return False
    return text[list_ind][char_ind-3:char_ind+1][::-1] == "XMAS"

def check_up(list_ind, char_ind, text):
    if list_ind - 3 < 0:
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind-1][char_ind] 
           + text[list_ind-2][char_ind] 
           + text[list_ind-3][char_ind]) == "XMAS"

def check_down(list_ind, char_ind, text):
    if list_ind + 3 >= len(text):
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind+1][char_ind] 
           + text[list_ind+2][char_ind] 
           + text[list_ind+3][char_ind]) == "XMAS"

def check_up_left(list_ind, char_ind, text):
    if list_ind - 3 < 0 or char_ind - 3 < 0:
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind-1][char_ind-1] 
           + text[list_ind-2][char_ind-2] 
           + text[list_ind-3][char_ind-3]) == "XMAS"

def check_up_right(list_ind, char_ind, text):
    if list_ind - 3 < 0 or char_ind + 3 >= len(text[list_ind]):
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind-1][char_ind+1] 
           + text[list_ind-2][char_ind+2] 
           + text[list_ind-3][char_ind+3]) == "XMAS"

def check_down_left(list_ind, char_ind, text):
    if list_ind + 3 >= len(text) or char_ind - 3 < 0:
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind+1][char_ind-1] 
           + text[list_ind+2][char_ind-2] 
           + text[list_ind+3][char_ind-3]) == "XMAS"

def check_down_right(list_ind, char_ind, text):
    if list_ind + 3 >= len(text) or char_ind + 3 >= len(text[list_ind]):
        return False
    return (text[list_ind][char_ind] 
           + text[list_ind+1][char_ind+1] 
           + text[list_ind+2][char_ind+2] 
           + text[list_ind+3][char_ind+3]) == "XMAS"


with open("input.txt") as f:
    inp = [line.strip() for line in f.readlines()]

total = 0
for ind_l, lst in enumerate(inp):
    for ind_c, c in enumerate(lst):
        if c == 'X':
            total += sum([
                check_right(ind_l, ind_c, inp),
                check_left(ind_l, ind_c, inp),
                check_up(ind_l, ind_c, inp),
                check_down(ind_l, ind_c, inp),
                check_up_left(ind_l, ind_c, inp),
                check_up_right(ind_l, ind_c, inp),
                check_down_left(ind_l, ind_c, inp),
                check_down_right(ind_l, ind_c, inp)
            ])

print(total)
