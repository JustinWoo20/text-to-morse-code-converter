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
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}

target = input('Would you like to convert to morse code or text?\n'
               'Please type "text" or "morse": ').lower()



def convert(direction):
    morse_code = ''
    converted_text = ''
    if direction == 'morse':
        text_to_con = input('Please type your text to convert to Morse Code: ').upper()
        try:
            for letter in text_to_con:
                morse_code += MORSE_CODE_DICT[letter]

        except KeyError:
            print(f'{letter} is not valid.\n'
                    f'Please try again.')

        else:
            print(morse_code)

    elif direction == 'text':
        morse_to_con = input('Please input your Morse Code as a series of periods and dashes: ')
        for symbol in morse_to_con:
            #Convert keys and values to their respective list
            morse_code_symbols = list(MORSE_CODE_DICT.values())
            morse_code_keys = list(MORSE_CODE_DICT.keys())

            #Find the index of the symbol
            symbol_loc = morse_code_symbols.index(symbol)

            #Use the index to match the symbol to the letter and add to the final text
            converted_text += morse_code_keys[symbol_loc]
        print(converted_text)

    else:
        print(f'{direction} is not a valid input.')
        print(f'Please try again and input either "morse" or "text".')

convert(direction=target)