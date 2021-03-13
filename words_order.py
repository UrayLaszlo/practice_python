def words_order(text, words):
    #a = ' '.join(words)
    l = []
    for i in text.split():
        if i in words:
            l.append(i)
    for elem in words:
        if words.count(elem) > 1:
            return False
    return l == words


words_order('hi here im here', ['here', 'here']) # False
words_order('hi world im here', ['world', 'here']) # True
words_order('hi world im here', ['here', 'world']) # False
words_order('hi world im here', ['world']) # True
words_order('hi world im here',
 ['world', 'here', 'hi']) # False
words_order('hi world im here',
 ['world', 'im', 'here']) # True
words_order('hi world im here',
 ['world', 'hi', 'here']) # False
words_order('hi world im here', ['world', 'world']) # False
words_order('hi world im here',
 ['country', 'world']) # False
words_order('hi world im here', ['wo', 'rld']) # False
words_order('', ['world', 'here']) # False