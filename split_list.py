def split_list(items):
    '''
    l = []
    mid_index = len(items) // 2
    if len(items) % 2 > 0:
        mid_index += 1
    f_h = items[:mid_index] 
    s_h = items[mid_index:]
    l.append(f_h)
    l.append(s_h)
    return l
    '''
    l = []
    if len(items) % 2 > 0:
        l.append(items[:(len(items)//2+1)])
        l.append(items[len(items)//2+1:])
    else:
        l.append(items[:len(items)//2]) 
        l.append(items[len(items)//2:])
    return l
split_list([1, 2, 3, 4, 5, 6]) # [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) # [[1, 2], [3]]
split_list([1, 2, 3, 4, 5]) # [[1, 2, 3], [4, 5]]
split_list([1]) # [[1], []]
split_list([]) # [[], []]