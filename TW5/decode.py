def encode(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        '''first while loop is for going through each letter'''
        count = 1
        ch = message[i]
        j = i  # assign current letter index to j in order to count the occurrence of letters
        print(ch)
        print('this is j', j)
        print('this is i ', i)
        while (j < len(message)-1):  # to loop from particular letter till the end
            # if char at the current index is the same as char at next index, the count is incremented by 1
            # if letters are equal to each other, keep looping, else break
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
    # the count and the character is concatenated to the encoded string
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string


def decode(message):
    decoded_message = ""
    i = 1
    for char in message:
        if char.isnumeric():
            if i < len(message):
                decoded_message += int(char) * message[i]
            i += 2
    return decoded_message


encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
print(decode(encoded_message))
