def popular_words(text, words):
    # your code here
    to_dict = {i : 0 for i in words}
    l = text.lower().split()
    for i in l:
        if i in to_dict:
            to_dict[i] += 1
    return to_dict



    # These "asserts" are used for self-checking and not for an auto-testing
popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }