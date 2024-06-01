def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97)
            decrypted_text += shifted_char.upper() if char.isupper() else shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            if shift < 0 or shift > 25:
                print("Shift value must be between 0 and 25.")
                continue
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (0-25): "))
            if shift < 0 or shift > 25:
                print("Shift value must be between 0 and 25.")
                continue
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
