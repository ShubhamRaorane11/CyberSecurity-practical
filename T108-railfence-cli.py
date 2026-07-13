def rail_fence_encrypt(text, rails):
    if rails <= 1 or not text:
        return text
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction_down = False
    for i in range(len(text)):
        if (rail == 0) or (rail == rails - 1):
            direction_down = not direction_down
        fence[rail][i] = text[i]
        rail += 1 if direction_down else -1
    return "".join([fence[i][j] for i in range(rails) for j in range(len(text)) if fence[i][j] != '\n'])

def rail_fence_decrypt(cipher, rails):
    if rails <= 1 or not cipher:
        return cipher
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]
    rail = 0
    direction_down = None
    for i in range(len(cipher)):
        if rail == 0: direction_down = True
        if rail == rails - 1: direction_down = False
        fence[rail][i] = '*'
        rail += 1 if direction_down else -1
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if (fence[i][j] == '*') and (index < len(cipher)):
                fence[i][j] = cipher[index]
                index += 1
    result, rail = [], 0
    for i in range(len(cipher)):
        if rail == 0: direction_down = True
        if rail == rails - 1: direction_down = False
        if fence[rail][i] != '\n':
            result.append(fence[rail][i])
            rail += 1 if direction_down else -1
    return "".join(result)

def main():
    print("=========================================")
    print("   Rail Fence Cipher(Transposition) - CLI Edition       ")
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
            rails = int(input("Enter number of rails (positive integer): "))
            if rails < 1: raise ValueError
        except ValueError:
            print("Error: Rails must be a positive integer.")
            continue
            
        if choice == '1':
            print(f"\nEncrypted Text: {rail_fence_encrypt(text, rails)}")
        else:
            print(f"\nDecrypted Text: {rail_fence_decrypt(text, rails)}")

if __name__ == "__main__":
    main()