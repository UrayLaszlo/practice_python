def order(sentence):
    new_string = [x for x in sentence.split()]
    return " ".join(sorted(new_string, key=lambda x :int("".join([i for i in x if i.isdigit()]))))
    # Alternative
    #return ' '.join(sorted(words.split(), key=lambda   w:sorted(w)))


order("is2 Thi1s T4est 3a")# "Thi1s is2 3a T4est")
order("4of Fo1r pe6ople g3ood th5e the2")# "Fo1r the2 g3ood 4of th5e pe6ople")
#order("")# "")