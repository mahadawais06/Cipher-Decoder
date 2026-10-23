import string

from caesar import caesar_decrypt

# Typical letter frequencies in English text, as percentages.
ENGLISH_FREQ: dict[str, float] = {
    "a": 8.2, "b": 1.5, "c": 2.8, "d": 4.3, "e": 12.7, "f": 2.2,
    "g": 2.0, "h": 6.1, "i": 7.0, "j": 0.15, "k": 0.77, "l": 4.0,
    "m": 2.4, "n": 6.7, "o": 7.5, "p": 1.9, "q": 0.095, "r": 6.0,
    "s": 6.3, "t": 9.1, "u": 2.8, "v": 0.98, "w": 2.4, "x": 0.15,
    "y": 2.0, "z": 0.074,
}


def count_letters(text: str) -> dict[str, int]:
    """Count how many times each letter a-z appears (case-insensitive)."""
    counts: dict[str, int] = {}
    for letter in string.ascii_lowercase:
        counts[letter] = 0
    for char in text.lower():
        if char in counts:
            counts[char] += 1
    return counts


def frequency_score(text: str) -> float:
    """Chi-squared distance from English. Lower = more English-like."""
    counts = count_letters(text)
    total = sum(counts.values())
    if total == 0:
        return float("inf")
    score = 0.0
    for letter in string.ascii_lowercase:
        expected = ENGLISH_FREQ[letter] / 100 * total
        score += (counts[letter] - expected) ** 2 / expected
    return score


def crack_caesar(ciphertext: str) -> tuple[int, str]:
    """Try all 26 shifts and return (shift, plaintext) that looks most English.

    The returned shift is the one that was used to encrypt the message.
    Works best on longer messages; very short ones can be ambiguous.
    """
    best_shift = 0
    best_score = float("inf")
    best_text = ciphertext
    for shift in range(26):
        candidate = caesar_decrypt(ciphertext, shift)
        score = frequency_score(candidate)
        if score < best_score:
            best_shift = shift
            best_score = score
            best_text = candidate
    return best_shift, best_text

