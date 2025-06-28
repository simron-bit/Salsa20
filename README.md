# Salsa20 Cipher Implementation in Python

##  Overview
In this code I have generated a ciphertext using Salsa20 encryption algorithm, which is a stream cipher. This is the second stream cipher that I have explored for my cryptography study.

##  Features
No external libraries have been used in the code. I have manually defined the key, nonce, counter block etc for better understanding of the algorithm.

##  Algorithm Description
1. In Salsa20 a 4x4 matrix is created with each element made up of 32 bits, thus the entire matrix comes out to be of 512 bits.
2. 10 quarter rounds( 1 quarter round= 1 column round + 1 diagonal round) are incorporated in Salsa20.
3. The transformed matrix generated after the 10 quarter rounds is added to the original matrix, thus creating a key stream of 512 bits(64 bytes).
4. This key stream is then XORed with the 64 bytes plaintext to generate the cipher text.

##  File Structure
 Salsa20.py

##  Requirements
python 3.x 

##  How to Run
You can run the file in any python environment

## Disclaimer
This code is strictly for educational purpose only. It is recommended to use this code to better understand different ciphers and their working structure. This code is neither intended nor optimised for security use.