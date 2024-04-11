
def encoder(password):
    encoded_password = ''
    for i in password:
        digit = int(i) + 3
        encoded_password += str(digit)
    return encoded_password



