def checkio(expression):
    brackets = ['(', ')', '[', ']', '{', '}']
    flag = False
    return any([x in brackets for x in expression])

checkio("2+3") #== True, "No brackets, no problem"
checkio("((5+3)*2+1)") #== True, "Simple"
checkio("{[(3+1)+2]+}") #== True, "Different types"
checkio("(3+{1-1)}") #== False, ") is alone inside {}"
checkio("[1+1]+(2*2)-{3/3}") #== True, "Different operators"
checkio("(({[(((1)-2)+3)-3]/3}-3)") #== False, "One is redundant"
