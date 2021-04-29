#from typing import Iterable
def is_ascending(items):
    # your code here
    '''
    new_list = []
    for i in items:
        if i not in new_list and sum(new_list) < sum(items):
            new_list.append(i)
        print(sum(items), sum(new_list))
    return items == new_list
    '''
    if len(items) < 2:
        return True
    else:
        for i in range(len(items)-1):
            print(items[i+1])
            if items[i] >= items[i+1]:
                return False
                break
        else:  
            return True

is_ascending([4, 5, 6, 7, 3, 7, 9]) #== False
is_ascending([-1,0,1]) # True
is_ascending([-5, 10, 99, 123456])# == True
is_ascending([99])# == True
is_ascending([])# == True
is_ascending([1, 1, 1, 1]) #== False