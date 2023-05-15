# Hooriya Amjad 30141172 Block 3
# hooriya.amjad@ucalgary.ca

import string

def main():                                                                             # main code 
    ''' 
        main

        parameters: none

        returns: none

        summary: asks for user choice to encode, decode or quit the program, 
        gets users text and cipher IF they want to encode or decode their text (choice not 0), 
        users entered cipher is made into all lowercase and removes duplicates if necessary,
        after choosing 1 to encode or 2 to decode, cipher is checked if its valid (alphanumeric and 26 elements),
        encode or decode cipher functions are called based on users choice IF users cipher is valid, 
        if users entered cipher is not valid, user is told to enter valid ciphers,
        loop runs until user chooses to quit program 
    '''

    while True:                                                                         # infinite while loop
        user_choice = int(input('Select 1 to encode, 2 to decode, or 0 to quit: '))     # prompt user choice
        if user_choice == 0:                                                            # if users choice is 0 break infinite loop
            print('Thank you for using this encryption program :)')
            break 
        user_text = input('Enter text to be processed: ')                               # if users choice is not 0 prompt user for text and cipher
        user_cipher = input('Enter cipher text: ')

        check_if_alphanum = user_cipher.isalnum()                                       # BONUS: check if the users cipher is alphanumeric, returns True or False     
        user_cipher = user_cipher.lower()                                               # BONUS: make users cipher elements lowercase
        user_cipher = ''.join(sorted(set(user_cipher), key=user_cipher.index))          # BONUS: remove any duplicates from the users cipher

        alphabet = string.ascii_lowercase                                               # set lowercase alphabet variable
        cipher_list = list(user_cipher)                                                 # make users cipher into list

        if user_choice == 1:
            if len(user_cipher) == 26 and check_if_alphanum is True:                    # if users choice is 1: cipher is 26 elements and cipher is alphanumeric:
                encoded_text = encode_cipher(alphabet, cipher_list, user_text)          # call encode cipher function
                print('Your cipher is valid')
                print('Your encoded text is:', encoded_text)                            # print cipher is valid and encoded text
                print()
            if len(user_cipher) != 26 or check_if_alphanum is False:                    # if users choice is 1: cipher is not 26 elements or cipher is not alphanumeric:
                print('Please enter valid cipher (26 unique elements of a-z or 0-9)')   # tell user to enter valid cipher
                print()

        if user_choice == 2:
            if len(user_cipher) == 26 and check_if_alphanum is True:                    # if users choice is 2: cipher is 26 elements and cipher is alphanumeric:
                decoded_text = decode_cipher(alphabet, cipher_list, user_text)          # call decode cipher function
                print('Your cipher is valid')
                print('Your decoded text is:', decoded_text)                            # print cipher is valid and decoded text
                print()
            if len(user_cipher) != 26 or check_if_alphanum is False:                    # if users choice is 2: cipher is not 26 elements or cipher is not alphanumeric:
                print('Please enter valid cipher (26 unique elements of a-z or 0-9)')   # tell user to enter valid cipher
                print()

def encode_cipher(alphabet, cipher_list, user_text):                                    # define encode function
    ''' 
        encode_cipher

        parameters: alphabet, cipher_list and user_text

        returns: encode_text
    
        summary: until all elements in users text are encoded, 
        each element in users text is found in the key(the alphabet) of the dictionary encode_dict
        and then replaced with the corresponding values(the users entered cipher) in encode_dict 
    '''

    encode_dict = dict(zip(alphabet, cipher_list))                                      # create dictionary with keys: alphabet, values: cipher text
    i = 0
    encode_text = ''
    while i < len(user_text):                                                           # while i is less than user text length: run loop
        if user_text[i] in encode_dict.keys():                                          # if i from user text is in dictionary key:
            encode_text += encode_dict[user_text[i]]                                    # replace with cipher value in dictionary
        i = i+1                                                                         # run until i is not < user text length
    return encode_text                                                                  # return encode text

def decode_cipher(alphabet, cipher_list, user_text):                                    # define decode function 
    ''' 
        decode cipher

        parameters: alphabet, cipher_list and user_text

        returns: decode_text
    
        summary: until all elements in users text are decoded, 
        each element in users text is found in the key(the users entered cipher) of the dictionary decode_dict
        and then replaced with the corresponding values(the alphabet) in decode_dict 
    '''

    decode_dict = dict(zip(cipher_list, alphabet))                                      # create dictionary with keys: cipher text, values: alphabet
    i = 0
    decode_text = ''
    while i < len(user_text):                                                           # while i is less than user text length: run loop
        if user_text[i] in decode_dict.keys():                                          # if i in user text is in dictionary keys:
            decode_text += decode_dict[user_text[i]]                                    # replace with alphabet value in dictionary
        i = i+1                                                                         # run until i is not < user text length
    return decode_text                                                                  # return decode text

main()                                                                                  # call main function


