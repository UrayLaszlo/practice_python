'''
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst
times_tables()
'''
l = [x * j for x in range(10) for j in range(10)]
