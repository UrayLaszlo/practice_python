def isometric_strings(str1, str2):
    # your code here
    m = set(zip(str1,str2))
    return len(set(str1)) == len(set(str2)) == len(set(zip(str1,str2)))

isometric_strings('add', 'egg')# == True
isometric_strings('foo', 'bar') #== False
isometric_strings('', '')# == True
isometric_strings('all', 'all')# == True
