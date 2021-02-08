def second_index(text, symbol):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    #print(text[text.find(symbol)+1:])
    #from_symbol = text[text.find(symbol)+1:]
    '''
    for i in range(len(from_symbol)):
        print(from_symbol)
        if from_symbol[i] == symbol:
            index_of_second = text.find(from_symbol[i],text.find(from_symbol))
    '''
    index_of_second = text.find(symbol,text.find(symbol)+1)
    if index_of_second < 1:
        index_of_second = None
    return index_of_second 

second_index("sims", "s") # 3, "First"
second_index("find the river", "e") # 12, "Second"
second_index("hi", " ") #is None, "Third"
second_index("hi mayor", " ") #is None, "Fourth"
second_index("hi mr Mayor", " ") # 5, "Fifth"