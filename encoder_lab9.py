
def encoder(password):
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




