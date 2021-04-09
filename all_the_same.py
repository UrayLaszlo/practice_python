#from typing import List, Any

def all_the_same(elements):
    l = []
    for i in elements:
        if i not in l:
            l.append(i)
    return len(l) < 2
    print(len(l))

all_the_same([1, 1, 1]) # True
all_the_same([1, 2, 1]) # False
all_the_same(['a', 'a', 'a']) # True
all_the_same([]) # True
all_the_same([1]) # True