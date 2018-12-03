#This program will allow you to decrypt or encrypt messages using a rail fence cipher

def encrypt(plainText):
    evenChars = ''
    oddChars= ''

    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch

        charCount = charCount + 1
    encrypted = oddChars + evenChars
    return encrypted

def decrypt(encrypted):
    halfLength = len(encrypted) // 2
    evenChars = encrypted[halfLength:]
    oddChars = encrypted[:halfLength]
    decrypted = ''
    for i in range(halfLength):
        decrypted = decrypted + evenChars[i]
        decrypted = decrypted + oddChars[i]
    if len(evenChars) > len(oddChars):
        decrypted = decrypted + evenChars[-1]
    
    return decrypted

def decision():
    choice = input('Would you like to encrypt or decrypt a message? ')
    if choice == 'encrypt' or choice == 'Encrypt':
        encryptmsg = encrypt(input('Please enter a message that you desire to encrypt: '))
        print(encryptmsg)
    elif choice == 'decrypt' or choice == 'Decrypt':
        decryptmsg = decrypt(input('Please enter a message that you desire to decrypt: '))
        print(decryptmsg)
    else:
        print('Please type encrypt or decrypt. ')
        decision()
decision()

input()
