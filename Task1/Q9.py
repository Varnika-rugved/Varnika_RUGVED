def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():  
            if ch.isupper():
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result
message = input("Enter a message: ")
shift_value = int(input("Enter shift value: "))

encrypted = caesar_cipher(message, shift_value)
print("Encrypted text:", encrypted)
