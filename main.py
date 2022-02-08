
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

string = input("Enter a word: ").upper()
#converting to Morse Code
def converter(str):
    
    try: 
        new_word = ''
        for letter in str:
            if letter != ' ':
                new_word += MORSE_CODE_DICT[letter] + ' '   
            else: 
                new_word += ' ' 
        return new_word
    except KeyError:
        return 'Cannot be Converted'

#converting from Morse Code 
def decipher(code):
    code += ' '
    decipher = ''
    letter_code = ''
    for i in code:
        if i != ' ':
            spaces = 0 
            letter_code += i
        else:
            spaces += 1
            if spaces == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter_code)]
                letter_code = ''
    return decipher

print(converter(string))

code = '-- --- .-. ... .  -.-. --- -.. .'
print(decipher(code))


