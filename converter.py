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
                    '0':'-----',}

# target = input('Would you like to convert to morse code or text?\n'
#                'Please type "text" or "morse": ').lower()

def convert():
    morse_code = ''
    # converted_text = ''
    text_to_con = input('Please type your text to convert to Morse Code: ').upper()
    try:
        for letter in text_to_con:
            if letter != ' ':
                # No space in the message indicates only one space in the Morse Code
                #Look up the Morse code in the dictionary
                morse_code += MORSE_CODE_DICT[letter] + ' '
            # If there is a space in the text we need 2 spaces in the Morse
            else:
                morse_code += '  '
    # Return an error message if the user inputs an invalid character
    except KeyError:
        print(f'{letter} is not valid.\n'
              f'Please try again.')

    print(morse_code)

convert()