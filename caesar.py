import string

def caesar_encrypt(text, shift):
    alphabet_list = list(string.ascii_lowercase)
    encrypted_text = ""
    for char in text:
        if char in alphabet_list:
            new_index = (alphabet_list.index(char) + shift) % 26
            encrypted_text += alphabet_list[new_index]
        else:
            if char in string.ascii_uppercase:
                new_index = (string.ascii_uppercase.index(char) + shift) % 26
                encrypted_text += string.ascii_uppercase[new_index]
            elif char in string.digits:
                new_index = (string.digits.index(char) + shift) % 10
                encrypted_text += string.digits[new_index]
            else:
                encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

