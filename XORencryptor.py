import os

def encrypt(filename, encryptionKey):
    with open(filename, "rb") as file:
        data = bytearray(file.read())

    for index, value in enumerate(data):
        data[index] = value ^ encryptionKey

    with open(filename + ".enc", "wb") as file_encrypted:
        file_encrypted.write(data)

    os.remove(filename)

def decrypt(filename, decryptionKey):
    with open(filename, "rb") as file:
        data = bytearray(file.read())

    for index, value in enumerate(data):
        data[index] = value ^ decryptionKey

    with open(filename[:-4], "wb") as file_decrypted:
        file_decrypted.write(data)

def main():
    mode = ""
    while mode != "3":
        print("Select an option:")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Exit")

        mode = input().strip()
        if mode == "1":
            filename = input("Enter filename to encrypt: ").strip()
            try:
                key = int(input("Enter encryption key (integer): "))
                encrypt(filename, key)
                print(f"{filename} encrypted successfully.")
            except ValueError:
                print("Invalid key. Please enter an integer.")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
            except Exception as e:
                print(f"Error encrypting '{filename}': {e}")

        elif mode == "2":
            filename = input("Enter filename to decrypt: ").strip()
            try:
                key = int(input("Enter decryption key (integer): "))
                decrypt(filename, key)
                print(f"{filename} decrypted successfully.")
            except ValueError:
                print("Invalid key. Please enter an integer.")
            except FileNotFoundError:
                print(f"Encrypted file '{filename}' not found.")
            except Exception as e:
                print(f"Error decrypting '{filename}': {e}")

        elif mode == "3":
            print("Exiting program...")
        else:
            print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
