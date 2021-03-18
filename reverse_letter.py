def reverse_letter(string):
    return "".join([x for x in string if x.isalpha()])[::-1]
    # Alternative
    # return ''.join(filter(str.isalpha, reversed(string)))

    

reverse_letter("krishan")#"nahsirk")
reverse_letter("ultr53o?n")#"nortlu")#
reverse_letter("ab23c")#"cba")
reverse_letter("krish21an")#"nahsirk")
