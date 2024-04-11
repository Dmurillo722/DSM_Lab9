def encode(password):
    encoded_password = ''
    for i in password:
        digit = int(i) + 3
        encoded_password += str(digit)
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_password += str((int(digit) - 3) % 10)
    return decoded_password


# Example usage:
encoded_password = "45678888"
decoded_password = decode(encoded_password)
print("Encoded Password:", encoded_password)
print("Decoded Password:", decoded_password)

while True:

    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()

    option = input('Please enter an option: ')

    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = (password)
        print('Your password has been encoded and stored!')
    elif option == '2':
        original_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')
    elif option == '3':
        break


   
