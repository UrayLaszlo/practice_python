def divisors(integer):
    '''
    integer_list = None
    if integer > 1:
        for i in range(2, integer):
            if (integer % i) == 0:
                integer_list = [i for i in range(2,integer) if not integer % i]
                break
        else:
            return str(integer) + " is prime"
    return integer_list
    '''
#  Alternative
    l = [a for a in range(2,integer) if integer%a == 0]
    if len(l) == 0:
        return str(integer) + " is prime"
    return l



divisors(15)#[3,5])
divisors(253)# [11,23])
divisors(24)#[2,3,4,6,8,12])
divisors(25)#[5])
divisors(13)#"13 is prime")
divisors(3)#"3 is prime")
divisors(29)#"29 is prime")