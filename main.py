# Encoder function to shift digits by 3
def encode(password: str) -> str:
    encoded = ''
    for char in password:
        # Shift each digit by 3
        encoded += str((int(char) + 3) % 10)
    return encoded

# Main function to interact with the user
def main():
    while True:
        print("\nMenu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        
        if option == '1':
            password = input("Please enter your password to encode (8 digits): ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print(f"Your password has been encoded and stored: {encoded_password}")
            else:
                print("Invalid input! Please enter an 8-digit number.")
        elif option == '2':
            print("Decode option selected. Decoder will be implemented by your partner.")
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
