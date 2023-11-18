from random import randrange

# function will return random number between start and end parameter where end is included
def rnd(start, end):
    return randrange(start, end+1)

# function should return the greatest number in a list
def max_num_in_list( lst ):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    
    return lst[-1]
        




