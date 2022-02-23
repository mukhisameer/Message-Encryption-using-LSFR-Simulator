Title : Message Encryption using LSFR Simulator

Technology : Python 3.8.7

General Info : 
The program encrypts and dcrypts messages using [N, k] LSFR [Linear Feedback Shift Register] and Base64 encoding. 

How to use:
1. Run the .py file to see an example of encryption and decryption.
2. To encrypt your own message change the content of the variable "original" in the main function.

How it works:
1. The program first converts each character of the message into decimal and then changes the decimal into binary using Base64 encoding.
2. The program then generates a sequence of psuedo-random numbers using the seed given as input to be used for LSFR.
3. The message is then encrypted using [N, k] LSFR. 

Note: This is a modified version of an assignment initially submitted for university coursework.