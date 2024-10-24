# Jonathan Stewart
# Encoder function to shift digits by 3
def encode(password: str) -> str:
    encoded = ''
    for char in password:
        # Shift each digit by 3
        encoded += str((int(char) + 3) % 10)
    return encoded

def decode(password_encoded):
    decoded = ""
    for char in password_encoded:
        original_digit = (int(char) - 3) % 10  
        decoded += str(original_digit)
    return decoded

# Main function
def main():
    encoded_password = None  # Variable to store the encoded password
    while True:
        print("\nMenu")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        
        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid input. Please enter an 8-digit number.")
        
        elif option == '2':
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
            else:
                print("No password has been encoded yet.")
        
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
