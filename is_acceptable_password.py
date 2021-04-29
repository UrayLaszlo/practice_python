def is_acceptable_password(str):
    # your code here
    flag = False
    for i in str:
        if i.isdigit():
            flag = True
            break
    elements = []
    for x in str:
        if x not in elements:
            elements.append(x)
            print(len(elements))
    if len(str) < 9:
        return len(str) > 6 and flag and not str.isnumeric() and not len(elements) < 3
    elif ('password' in str or 'PASSWORD' in str) or len(elements) < 3:
        return False
    else:
        return True


is_acceptable_password('aaaaaa1') #== False
is_acceptable_password('aaaaaabbbbb') #== False
'''
is_acceptable_password('short') #== False
is_acceptable_password('muchlonger')# == True
is_acceptable_password('short54')# == True
is_acceptable_password('ashort') #== False
is_acceptable_password('muchlonger5')# == True
is_acceptable_password('sh5') #== False
is_acceptable_password('1234567') #== False
is_acceptable_password('12345678910')# == True
is_acceptable_password('password12345') #== False
is_acceptable_password('PASSWORD12345') #== False
is_acceptable_password('pass1234word')# == True
is_acceptable_password('aaaaaabb1')# == True
is_acceptable_password('abc1') #== False
is_acceptable_password('abbcc12')# == True
'''