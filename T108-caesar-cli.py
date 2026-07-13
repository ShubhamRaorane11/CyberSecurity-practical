def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=========================================")
    print("   Caesar Cipher - CLI Edition           ")
    print("=========================================")
    
    while True:
        print("\n[1] Encrypt a Message")
        print("[2] Decrypt a Message")
        print("[3] Exit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '3':
            print("Goodbye!")
            break
            
        if choice not in ['1', '2']:
            print("Invalid selection. Please choose 1, 2, or 3.")
            continue
            
        text = input("Enter the text: ")
        try:
            shift = int(input("Enter shift key (integer): "))
        except ValueError:
            print("Error: Shift key must be an integer.")
            continue
            
        if choice == '1':
            print(f"\nEncrypted Text: {caesar_encrypt(text, shift)}")
        else:
            print(f"\nDecrypted Text: {caesar_decrypt(text, shift)}")

if __name__ == "__main__":
    main()