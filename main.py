import hashlib
import time
import binascii

# Function to process each 64-byte chunk of the input data
def process_chunk(chunk, h0, h1, h2, h3, h4):
    # Ensure that the chunk is 64 bytes long
    assert len(chunk) == 64

    # Divide the chunk into sixteen 4-byte big-endian words
    words = [int.from_bytes(chunk[i:i+4], 'big') for i in range(0, 64, 4)]
    
    # Extend the sixteen words into eighty 32-bit words
    words += [0] * (80 - 16)
    for i in range(16, 80):
        words[i] = left_rotate(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1)

    # Initialize the hash value for this chunk
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4

    # Main loop, applying the compression function to update the hash value
    for i in range(80):
        if i <= 19:
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif i <= 59:
            f = (b & c) | (d & (b | c))
            k = 0x8F1BBCDC
        else:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        a, b, c, d, e = left_rotate(a, 5) + f + e + k + words[i] & 0xFFFFFFFF, \
                         a, left_rotate(b, 30), c, d

    # Add this chunk's hash to result so far
    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF

    return h0, h1, h2, h3, h4

# Main SHA-1 function
def sha1(data):
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing (padding and length extension)
    length = len(data) * 8
    data += b'\x80'
    while len(data) % 64 != 56:
        data += b'\x00'
    data += length.to_bytes(8, 'big')

    # Process the message in successive 512-bit chunks
    for i in range(0, len(data), 64):
        h0, h1, h2, h3, h4 = process_chunk(data[i:i+64], h0, h1, h2, h3, h4)

    # Return the final hash value
    return (h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4).to_bytes(20, 'big')

# Auxiliary function to perform left bitwise rotation
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

if __name__ == "__main__":
    # Get input from user
    data = input("Enter the data to be hashed: ").encode('utf-8')

    # Calculate time for your function
    start_time = time.time()
    my_hash = sha1(data)
    end_time = time.time()
    my_time = round(end_time - start_time, 4)

    print("------------------------------------------------------------------------")
    print(f"| My SHA-1 hash value: | {binascii.hexlify(my_hash).decode()} |")

    # Calculate time for hashlib
    start_time = time.time()
    hashlib_hash = hashlib.sha1(data).digest()
    end_time = time.time()
    hashlib_time = round(end_time - start_time, 4)

    print("------------------------------------------------------------------------")
    print(f"| Hashlib SHA-1 hash value: | {binascii.hexlify(hashlib_hash).decode()} |")
    print("------------------------------------------------------------------------\r\n")

    # Compare times
    comparison = "faster" if my_time < hashlib_time else "slower"
    print(f"My SHA-1 implementation is {comparison} than hashlib's implementation by {abs(my_time - hashlib_time)} seconds.\r\n")

    # Compare hashes
    match = "match" if my_hash == hashlib_hash else "do not match"
    print(f"The calculated hashes {match}.")
