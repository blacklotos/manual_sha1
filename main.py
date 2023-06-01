import hashlib
import struct
import time

def process_chunk(chunk, h0, h1, h2, h3, h4):
    assert len(chunk) == 64

    words = [int.from_bytes(chunk[i:i+4], 'big') for i in range(0, 64, 4)]
    words += [0] * (80 - 16)
    for i in range(16, 80):
        words[i] = left_rotate(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1)

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4

    for i in range(80):
        if 0 <= i <= 19:
            f = d ^ (b & (c ^ d))
            k = 0x5A827999
        elif 20 <= i <= 39:
            f = b ^ c ^ d
            k = 0x6ED9EBA1
        elif 40 <= i <= 59:
            f = (b & c) | (d & (b | c))
            k = 0x8F1BBCDC
        elif 60 <= i <= 79:
            f = b ^ c ^ d
            k = 0xCA62C1D6

        a, b, c, d, e = left_rotate(a, 5) + f + e + k + words[i] & 0xFFFFFFFF, \
                         a, left_rotate(b, 30), c, d

    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF

    return h0, h1, h2, h3, h4

def sha1(data):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing:
    length = len(data) * 8
    data += b'\x80'
    while len(data) % 64 != 56:
        data += b'\x00'
    data += length.to_bytes(8, 'big')

    # Process the message in successive 512-bit chunks:
    for i in range(0, len(data), 64):
        h0, h1, h2, h3, h4 = process_chunk(data[i:i+64], h0, h1, h2, h3, h4)

    return (h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4).to_bytes(20, 'big')


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

# Test data
data = "Hello, world!".encode('utf-8')

# Calculate time for your function
start_time = time.time()
my_hash = sha1(data)
print (my_hash)
end_time = time.time()
my_time = end_time - start_time
print("My function took", my_time, "seconds")

# Calculate time for hashlib
start_time = time.time()
hashlib_hash = hashlib.sha1(data).digest()
print (hashlib_hash)
end_time = time.time()
hashlib_time = end_time - start_time
print("Hashlib function took", hashlib_time, "seconds")

# Compare times
if my_time < hashlib_time:
    print("My function is faster")
elif my_time > hashlib_time:
    print("Hashlib function is faster")
else:
    print("Both functions have the same speed")

# Compare hashes
if my_hash == hashlib_hash:
    print("Hashes match")
else:
    print("Hashes do not match")
