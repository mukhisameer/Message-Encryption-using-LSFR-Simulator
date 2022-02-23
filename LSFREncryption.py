

# To convert a decimal value to binary, returning it in a list form
def decToBin(x, n = 6):
    binary = []
    while (x > 0):
        binary.append(0 if x % 2 == 0 else 1)
        x = int(x / 2)
    while (len(binary) < n):
        binary.append(0)
    binary.reverse()
    return binary

# To convert a binary value in list form to decimal
def binToDec(binary):
    dec = 0
    power = 1
    length = len(binary)
    for i in range(1, length + 1):
        dec += binary[length - i] * power
        power = power * 2
    return dec

# Using Base64 encoding to convert a character into binary
def charToBin(c):
    char_dec = ord(c)
    if char_dec > 64 and char_dec <= 90:
        char_dec -= 65
    elif char_dec > 90:
        char_dec -= 71
    elif char_dec == 43:
        char_dec += 19
    elif char_dec == 47:
        char_dec += 16
    elif char_dec >= 48 and char_dec <= 57:
        char_dec += 4
    char_bin = decToBin(char_dec)
    return char_bin

# Using Base64 encoding to convert a list of binary digits into a character
def binToChar(b):
    char_dec = binToDec(b)
    if char_dec <= 25:
        char_dec += 65
    elif char_dec > 25 and char_dec <= 51 :
        char_dec += 71
    elif char_dec == 62:
        char_dec -= 19
    elif char_dec == 63:
        char_dec -= 16
    elif char_dec >= 52 and char_dec <= 61:
        char_dec -= 4
    return chr(char_dec)

# Using Base64 encoding to convert a string into a binary list
def strToBin(s):
    binary_list = []
    for char in s:
        binary_list.extend(charToBin(char))
    return binary_list

# Using Base64 encoding to convert a list of binary digits into a string
def binToStr(b_list):
    divided_list = []
    word = ''
    for i in range(0, len(b_list), 6):
        divided_list.append(b_list[i:i+6])
    for sublist in divided_list:
        word += (binToChar(sublist))
    return word

# A function to generate a sequence of psuedo-random numbers to be used for encryption
def generatePad(seed, k, length):
    pad = []
    while length > 0:
        if seed[0] == seed[-k]:
            seed.append(0)
            pad.append(0)
        else:
            seed.append(1)
            pad.append(1)
        seed.pop(0)
        length -= 1
    return pad

# Using [N, k] LFSR to encrypt the message given as input
def encrypt(message, seed, k):
    bin_message = strToBin(message)
    pad = generatePad(seed, k, len(bin_message))
    encrypted_bin = []
    index = 0
    while index < len(bin_message):
        if bin_message[index] == pad[index]:
            encrypted_bin.append(0)
        else:
            encrypted_bin.append(1)
        index += 1
    encrypted_message = binToStr(encrypted_bin)
    return encrypted_message

def main():

	print("Testing Encryption")
	original = "ILikePython"
	encrypted = encrypt(original, [1,0,1,0,0,1,0,0,1,0], 8)
	print("Orignal Message:   ", original)
	print("Encrypted Message: ", encrypted)

	print("\nTesting Decryption")
	decrypted = encrypt(encrypted, [1,0,1,0,0,1,0,0,1,0], 8)
	print("Encrypted Message  :", encrypted)
	print("Decrypted Message  :", decrypted, "\n")

main()