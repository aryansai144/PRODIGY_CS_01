def encrypt(text, shift_value):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift_value) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift_value):
    return encrypt(text, -shift_value)


while True:
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
        continue

    message = input("Enter your message: ")
    try:
        shift_value = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        continue

    if choice == 'e':
        encrypted_message = encrypt(message, shift_value)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift_value)
        print(f"Decrypted message: {decrypted_message}")

    again = input("Do you want to process another message? (yes/no): ").lower()
    if again != 'yes':
        break

