#import collections
#from itertools import repeat, chain
def frequency_sort(items):
    # your code here
    '''
    l = []
    count_i = 0
    for i in items:
        count_i = items.count(i)
        if items.count(i) > count_i:
            l.append(i)
    '''
    #m = max(items)
    #return sorted(items,key=items.count,reverse=True)
    '''
    l = set([x for x in items if items.count(x) > 1])
    print(len(l))
    if len(l) < 1:
        return items
    else: 
        return sorted(items, key=lambda x: (collections.Counter(items)[x], x), reverse=False)
    '''
#    result = list(chain.from_iterable(repeat(i, c)
#         for i, c in collections.Counter(items).most_common()))
 
    '''
    l = []
    for x in items:
        if items.count(x) >= 2:
            l.append(x)
        else:
            frequency_sort(l)
    return l
    '''
    '''OTHER SOLUTION
    def frequency_sort(items):
    
    items_unique = [] 
      
    for x in items:                     # loop to find unique items
        if x not in items_unique: 
            items_unique.append(x) 
       
    counts = []
            
    for x in items_unique:              # loop to find the count per unique item
        count = items.count(x)
        counts.append(count)
        
    output = []
        
    for i in range(len(counts)):        # loop to add each item to the output the correct number of times
        maxcount = max(counts)
        maxind = counts.index(maxcount)
        
        output += [items_unique[maxind]]*maxcount
        counts[maxind] = 0
    
    return output
    '''
    #OTHER SOLUTION
def frequency_sort(items):
    temp = sorted(items,key = lambda x:items.count(x),reverse =True)
    return sorted(temp,key = lambda x:temp.index(x))

        
    # These "asserts" are used for self-checking and not for an auto-testing
frequency_sort([1,2,2,1])
frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) # [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) # ['bob', 'bob', 'bob', 'carl', 'alex']
frequency_sort([17, 99, 42]) # [17, 99, 42]
frequency_sort([]) # []
frequency_sort([1]) # [1]