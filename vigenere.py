import string

from caesar import caesar_encrypt


def is_valid_vigenere_key(key: str) -> bool:
    """A key must be non-empty and contain only letters."""
    for char in key:
        if char not in string.ascii_letters:
            return False
    return len(key) > 0


def vigenere_shift(text: str, key: str, direction: int) -> str:
    """direction = 1 encrypts, direction = -1 decrypts.

    Each letter of `key` is a Caesar shift (a=0, b=1, ...). The key only
    advances on letters, so spaces and punctuation don't use up key letters.
    """
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char in string.ascii_letters:
            shift = string.ascii_lowercase.index(key[key_index % len(key)])
            result += caesar_encrypt(char, shift * direction)
            key_index += 1
        else:
            result += char
    return result


def vigenere_encrypt(text: str, key: str) -> str:
    return vigenere_shift(text, key, 1)


def vigenere_decrypt(text: str, key: str) -> str:
    return vigenere_shift(text, key, -1)

