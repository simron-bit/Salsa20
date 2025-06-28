#Salsa20 cipher
plaintext=b"this is a dummy plaintext"

#Step 1: Define key,nonce,block counter and constants
key=bytes([0x01, 0x02, 0x03, 0x04] * 8 ) 
nonce=bytes([0x02, 0x04, 0x06, 0x07, 0x09, 0x03, 0x02, 0x01])
b0=bytes([0x06, 0x01, 0x07, 0x08])
b1=bytes([0x01, 0x08, 0x09, 0x03])
constant_str =b"expand 32-byte k"  

#Step 2: Define the elements of the matrix
k0=int.from_bytes(key[0:4],'little')
k1=int.from_bytes(key[4:8],'little')
k2=int.from_bytes(key[8:12],'little')
k3=int.from_bytes(key[12:16],'little')
k4=int.from_bytes(key[16:20],'little')
k5=int.from_bytes(key[20:24],'little')
k6=int.from_bytes(key[24:28],'little')
k7=int.from_bytes(key[28:32],'little')

n0=int.from_bytes(nonce[0:4],'little')
n1=int.from_bytes(nonce[4:8],'little')

b0=int.from_bytes(b0[0:4],'little')
b1=int.from_bytes(b1[0:4],'little')

c0=int.from_bytes(constant_str[0:4],'little')
c1=int.from_bytes(constant_str[4:8],'little')
c2=int.from_bytes(constant_str[8:12],'little')
c3=int.from_bytes(constant_str[12:16],'little')

#Step 3: Build the state
state=[c0,k0,k1,k2,
       k3,c1,b0,b1,
       c2,n0,n1,k4,
       k5,k6,k7,c3]

original=[c0,k0,k1,k2,
       k3,c1,b0,b1,
       c2,n0,n1,k4,
       k5,k6,k7,c3]

#Step 4: The Quater round (1 quater round= 1 coloumn round + 1 diagonal round)
def rotate_left(x, n):
        return ((x << n) | (x >> (32 - n))) & 0xffffffff
    
def quarter_round(a, b, c, d):
        b ^= rotate_left((a + d) & 0xffffffff, 7)
        c ^= rotate_left((b + a) & 0xffffffff, 9)
        d ^= rotate_left((c + b) & 0xffffffff, 13)
        a ^= rotate_left((d + c) & 0xffffffff, 18)
        return a, b, c, d

for k in range(10):
        for j in range(4):
          a=state[j]
          b=state[j+4]
          c=state[j+8]
          d=state[j+12]

          a,b,c,d=quarter_round(a,b,c,d)
    
          state[j]=a
          state[j+4]=b
          state[j+8]=c
          state[j+12]=d
    
        a=state[0]
        b=state[5]
        c=state[10]
        d=state[15]

        a,b,c,d=quarter_round(a,b,c,d)

        state[0]=a
        state[5]=b
        state[10]=c
        state[15]=d

        a=state[1]
        b=state[6]
        c=state[11]
        d=state[12]

        a,b,c,d=quarter_round(a,b,c,d)

        state[1]=a
        state[6]=b
        state[11]=c
        state[12]=d

        a=state[2]
        b=state[7]
        c=state[8]
        d=state[13]

        a,b,c,d=quarter_round(a,b,c,d)

        state[2]=a
        state[7]=b
        state[8]=c
        state[13]=d

        a=state[3]
        b=state[4]
        c=state[9]
        d=state[14]

        a,b,c,d=quarter_round(a,b,c,d)

        state[3]=a
        state[4]=b
        state[9]=c
        state[14]=d

#Step 5: Generation of the key-stream
key_stream = [(state[i] + original[i]) & 0xffffffff for i in range(16)]
key_stream_bytes = b''.join(x.to_bytes(4, 'little') for x in key_stream)

#Step 6: Generation of ciphertext
ciphertext=bytes([p ^ k for p, k in zip(plaintext, key_stream_bytes)])
       
print("Ciphertext:",ciphertext)