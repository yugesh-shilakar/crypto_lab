#ENCRYPTION
def encrypt(plaintext, shift):
  ciphertext = ""
  
  for ch in plaintext:
    if ch.isalpha():
      shift_ch = chr((ord(ch) + shift - 97) % 26 + 97)
      ciphertext += shift_ch
    else:
      ciphertext += ch

  return ciphertext


#DECRYPTION
def decrypt(ciphertext, shift):
  plaintext = ""

  for ch in ciphertext:
    if ch.isalpha():
      shift_ch = chr((ord(ch) - shift - 97) % 26 + 97)
      plaintext += shift_ch
    else:
      plaintext += ch

  return plaintext

#TEST

plaintext = "yugesh"
shift = 3

ciphertext = encrypt(plaintext, shift)
print("Encrypted:",ciphertext)

decrypted_text = decrypt(ciphertext, shift)
print("Decrypted:",decrypted_text)
