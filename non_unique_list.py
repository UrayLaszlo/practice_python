def checkio(list):
    new_list = []
    for i in list:
        if list.count(i) > 1:
            new_list.append(i)
    
    return new_list



checkio([1, 2, 3, 1, 3]) # [1, 3, 1, 3], "1st example"
checkio([1, 2, 3, 4, 5]) # [], "2nd example"
checkio([5, 5, 5, 5, 5]) # [5, 5, 5, 5, 5], "3rd example"
checkio([10, 9, 10, 10, 9, 8]) # [10, 9, 10, 10, 9], "4th example"