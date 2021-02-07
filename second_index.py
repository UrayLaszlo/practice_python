def second_index(text, symbol):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    index_of_second = None
    print(text[text.find(symbol)+1:])
    for i in text[text.find(symbol)+1:]:
        print(i)
        if i == symbol:
            index_of_second = text.find(i)
    
    return index_of_second

second_index("sims", "s") # 3, "First"
second_index("find the river", "e") # 12, "Second"
second_index("hi", " ") #is None, "Third"
second_index("hi mayor", " ") #is None, "Fourth"
second_index("hi mr Mayor", " ") # 5, "Fifth"