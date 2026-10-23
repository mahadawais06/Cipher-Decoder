import string


def is_valid_key(key: str) -> bool:
    """A valid key uses each of the 26 letters exactly once."""
    return sorted(key.lower()) == list(string.ascii_lowercase)


def substitution_encrypt(text: str, key: str) -> str:
    """Replace each letter with the letter at the same position in `key`."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    key = key.lower()
    result = ""
    for char in text:
        if char in lower:
            result += key[lower.index(char)]
        elif char in upper:
            result += key[upper.index(char)].upper()
        else:
            result += char
    return result


def substitution_decrypt(text: str, key: str) -> str:
    """Reverse the mapping: find each letter's position in `key`."""
    lower = string.ascii_lowercase
    key = key.lower()
    result = ""
    for char in text:
        if char.lower() in key and char.isalpha():
            position = key.index(char.lower())
            if char.isupper():
                result += lower[position].upper()
            else:
                result += lower[position]
        else:
            result += char
    return result
