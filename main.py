from caesar import caesar_decrypt, caesar_encrypt
from cracker import crack_caesar
from substitution import is_valid_key, substitution_decrypt, substitution_encrypt
from vigenere import is_valid_vigenere_key, vigenere_decrypt, vigenere_encrypt

MENU = """
=== CipherLab ===
1) Caesar encrypt
2) Caesar decrypt
3) Caesar crack (no key needed)
4) Substitution encrypt
5) Substitution decrypt
6) Vigenere encrypt
7) Vigenere decrypt
0) Quit
"""


def ask_int(prompt: str) -> int:
    """Keep asking until the user enters a whole number."""
    answer = input(prompt)
    try:
        return int(answer)
    except ValueError:
        print("Please enter a whole number.")
        return ask_int(prompt)


def ask_substitution_key() -> str:
    key = input("Enter 26-letter key (each letter once): ")
    if is_valid_key(key):
        return key
    print("Invalid key. It must use each letter a-z exactly once.")
    return ask_substitution_key()


def ask_vigenere_key() -> str:
    key = input("Enter key word (letters only): ")
    if is_valid_vigenere_key(key):
        return key
    print("Invalid key. Use letters only.")
    return ask_vigenere_key()


def main() -> None:
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            return

        if choice not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Invalid choice, try again.")
            continue

        text = input("Enter text: ")

        if choice == "1":
            print("Result:", caesar_encrypt(text, ask_int("Shift: ")))
        elif choice == "2":
            print("Result:", caesar_decrypt(text, ask_int("Shift: ")))
        elif choice == "3":
            shift, plaintext = crack_caesar(text)
            print(f"Most likely shift: {shift}")
            print("Result:", plaintext)
        elif choice == "4":
            print("Result:", substitution_encrypt(text, ask_substitution_key()))
        elif choice == "5":
            print("Result:", substitution_decrypt(text, ask_substitution_key()))
        elif choice == "6":
            print("Result:", vigenere_encrypt(text, ask_vigenere_key()))
        elif choice == "7":
            print("Result:", vigenere_decrypt(text, ask_vigenere_key()))


if __name__ == "__main__":
    main()
