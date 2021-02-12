from string import ascii_lowercase
# UNFINISHED
def rank(st, we, n):
    # your code
    if not st:
        return 'No participants'
    print(len(list(st)))
    if n > len(list(st)):
        return 'Not enough participants'
    name = ''

    LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

    def alphabet_position(text):
        text = text.lower()

        numbers = [LETTERS[character] for character in text if character in LETTERS]

        return ' '.join(numbers)

    char = [chr(i) for i in range(ord('a'),ord('z')+1)]
    nums = range(26)

    return name


rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)# "Benjamin")
rank("Lagon,Lily", [1, 5], 2)# "Lagon")
rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8)# "Not enough participants")
rank("", [4, 2, 1, 4, 3, 1, 2], 6)#"No participants")