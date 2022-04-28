#AN TAN NGUYEN 

def mc_converter(text):
    MC_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',  '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/', "'": "'", '-': '-' }

    morse_code = ""
    
    for i in text:
        morse_code = morse_code + MC_DICT[i.upper()]

    revmorse_code = morse_code[::-1]

    if morse_code.strip( ) == "":
        return "NO"
    elif morse_code == revmorse_code:
        return "YES"
    elif morse_code == "-.----":
        return "Goodbye"
    else:
        return "NO"


pal = 0
while pal != "-1":
    pal = input("Enter a string of characters to check if it is a palindrome in morse code. (Enter -1 to stop) ")

    print(mc_converter(pal))
















