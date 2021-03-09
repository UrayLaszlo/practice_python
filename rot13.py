import codecs
def rot13(message):
    '''
    alphabet = {
        'a' : 'n', 
        'b' : 'o', 
        'c' : 'p', 
        'd' : 'q', 
        'e' : 'r', 
        'f' : 's', 
        'g' : 't', 
        'h' : 'u', 
        'i' : 'v', 
        'j' : 'w', 
        'k' : 'x', 
        'l' : 'y', 
        'm' : 'z', 
        'n' : 'a', 
        'o' : 'b', 
        'p' : 'c', 
        'q' : 'd', 
        'r' : 'e', 
        's' : 'f', 
        't' : 'g', 
        'u' : 'h', 
        'v' : 'i', 
        'w' : 'j', 
        'x' : 'k', 
        'y' : 'l', 
        'z' : 'm',
        'A' : 'N', 
        'B' : 'O', 
        'C' : 'P', 
        'D' : 'Q', 
        'E' : 'R', 
        'F' : 'S', 
        'G' : 'T', 
        'H' : 'U', 
        'I' : 'V', 
        'J' : 'W', 
        'K' : 'X', 
        'L' : 'Y', 
        'M' : 'Z', 
        'N' : 'A', 
        'O' : 'B', 
        'P' : 'C', 
        'Q' : 'D', 
        'R' : 'E', 
        'S' : 'F', 
        'T' : 'G', 
        'U' : 'H', 
        'V' : 'I', 
        'W' : 'J', 
        'X' : 'K', 
        'Y' : 'L', 
        'Z' : 'M'
    }
    for k,v in alphabet.items():
        if k in message_list:
            k = v
            message_13.append(v)
    for i in message:
        if not i.isalpha():
            message_13.append(i)
    return message_13
    '''
    '''
    message_list = [i for i in message]
    message_13 = []
    alphabet = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i in message_list:
        pos = message_list.index(i) + 13
        message_13.append(i)
    '''
    return codecs.encode(message, "rot13")

rot13("EBG13 rknzcyr.")# "ROT13 example.")
rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")# "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
#rot13("123")# "123")
#rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)")# "This is actually the first kata I ever made. Thanks for finishing it! :)")
#rot13("@[`{")# "@[`{")