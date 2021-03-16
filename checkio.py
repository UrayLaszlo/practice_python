def checkio(number):
    n = [int(x) for x in str(number) if x != '0']
    #m = [x for x in n if x != 0]
    m = 1
    for i in n:
        m *= i 
    return m

checkio(123405) # 120
checkio(999) # 729
checkio(1000) # 1
checkio(1111) # 1