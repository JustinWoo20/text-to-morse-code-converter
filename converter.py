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
                    '(':'-.--.', ')':'-.--.-',}

# test_message = '.... . .-.. .-.. ---  .-- --- .-. .-.. -..'
# User chooses whether to encrypt or decrypt
target = input('Would you like to encrypt to Morse Code or decrypt to Morse Code?\n'
               'Please type "encrypt" or "decrypt" to choose a direction: ').lower()

def direction(user_choice):
    # Choose whether to encrypt or decrypt
    if user_choice== 'encrypt':
        result = encrypt()
    elif user_choice == 'decrypt':
        result = decrypt()
    else:
        print(f'{user_choice} is not a valid input.')
        print(f'Please try again and input either "morse" or "text".')
        return None

    return result

def encrypt():
    morse_code = ''
    text_to_con = input('Please type your text to convert to Morse Code: ').upper()
    try:
        for letter in text_to_con:
            if letter != ' ':
                # No space in the message indicates only one space in the Morse Code
                # Look up the Morse code in the dictionary
                morse_code += MORSE_CODE_DICT[letter] + ' '
            # If there is a space in the text we need 2 spaces in the Morse Code
            else:
                morse_code += '  '
    # Return an error message if the user inputs an invalid character
    except KeyError:
        print(f'{letter} is not valid.\n'
              f'Please try again.')

    return morse_code

def decrypt():
    decrypted_text = ''
    # Convert keys and values to their respective lists
    morse_code_symbols = list(MORSE_CODE_DICT.values())
    morse_code_keys = list(MORSE_CODE_DICT.keys())
    morse_to_con = input('Please input your Morse Code as a series of periods and dashes: ')
    # Hard coded message for debugging
    # morse_to_con = test_message
    # Record each set of symbols to match to the dictionary later
    morse_text = ''
    # Keep track of spaces to distinguish where words begin and end
    i = 0
    try:
        for symbol in morse_to_con:
            if i == 1 and symbol != ' ':
                # If we have a new symbol while i = 1 then we know it's the start of a new letter
                # We need to find that letter and add it to the decrypted text
                # Find the index of the Morse Code
                symbol_loc = morse_code_symbols.index(morse_text)
                # Use the index to match the symbol to the letter and add to the final text
                decrypted_text += morse_code_keys[symbol_loc]
                # Reset the symbol tracker
                morse_text = ''
                morse_text += symbol
                i = 0

            elif symbol != ' ':
                morse_text += symbol

            else:
                i += 1
                if i == 2:
                    symbol_loc = morse_code_symbols.index(morse_text)
                    # New word
                    decrypted_text += morse_code_keys[symbol_loc] + " "
                    morse_text = ''
                    i = 0
        # Run this one more time to get the last letter
        symbol_loc = morse_code_symbols.index(morse_text)
        decrypted_text += morse_code_keys[symbol_loc]

    except KeyError:
        print(f'{symbol} is not valid.\n'
              f'Please try again.')

    return decrypted_text

print(direction(user_choice=target))