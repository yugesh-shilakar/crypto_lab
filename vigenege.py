message = "yugesh"
key = "crypto"
 
# ENCRYPTION
def vigenere_cipher(message, key):
    # Convert the message and key to lowercase letters
    message = message.lower()
    key = key.lower()
 
    # Create a list to store the encrypted message
    encrypted_message = []
 
    # Loop through each letter in the message
    for i, letter in enumerate(message):
        # If the letter is not alphabetical, don't encrypt it
        if not letter.isalpha():
            encrypted_message.append(letter)
            continue
 
        # Get the ASCII code for the letter and the key
        letter_code = ord(letter) - 97
        key_code = ord(key[i % len(key)]) - 97
 
        # Use the Vigenère cipher formula to encrypt the letter
        encrypted_code = (letter_code + key_code) % 26
        encrypted_letter = chr(encrypted_code + 97)
 
        # Append the encrypted letter to the encrypted message
        encrypted_message.append(encrypted_letter)
 
    # Convert the encrypted message list to a string and return it
    return ''.join(encrypted_message)
 
 
 
encrypted_message = vigenere_cipher(message, key)
print ("Encrypted:",encrypted_message)
 
 
# DECRYPTION
def vigenere_decrypt(encrypted_message, key):
    # Convert the encrypted message and key to lowercase letters
    encrypted_message = encrypted_message.lower()
    key = key.lower()
 
    # Create a list to store the decrypted message
    decrypted_message = []
 
    # Loop through each letter in the encrypted message
    for i, letter in enumerate(encrypted_message):
        # If the letter is not alphabetical, don't decrypt it
        if not letter.isalpha():
            decrypted_message.append(letter)
            continue
 
        # Get the ASCII code for the letter and the key
        letter_code = ord(letter) - 97
        key_code = ord(key[i % len(key)]) - 97
 
        # Use the Vigenère cipher formula to decrypt the letter
        decrypted_code = (letter_code - key_code) % 26
        decrypted_letter = chr(decrypted_code + 97)
 
        # Append the decrypted letter to the decrypted message
        decrypted_message.append(decrypted_letter)
 
    # Convert the decrypted message list to a string and return it
    return ''.join(decrypted_message)
 
decrypted_message = vigenere_decrypt(encrypted_message, key)
print("Decrypted:",decrypted_message)