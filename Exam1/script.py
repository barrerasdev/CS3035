# Juan Barreras
# CS 3035-01 Exam I Part II

# My Tests:
#  distance: 3
#  plaintext: hello
#  encryptedtext: khoor

def encrypt(text, distance):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted = ord(char) + distance
            if shifted > 122:
                shifted -= 26
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(text, distance):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted = ord(char) - distance
            if shifted < 97:
                shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

distance = int(input("input the distance: "))
plaintext = input("input a plain text string: ")
encryptedtext = input("input an encrypted string: ")

encrypted = encrypt(plaintext, distance)
decrypted = decrypt(encryptedtext, distance)

print("\nResults:")
print("plain text input: ", plaintext)
print("encrypted:  ", encrypted)
print("encrypted input: ", encryptedtext)
print("decrypted:  ", decrypted)

# Results from terminal: 
#  plain text: hello
#  encrypted: khoor
#  encrypted input: khoor
#  decrypted: hello