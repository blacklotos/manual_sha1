# Python SHA-1 Implementation

This project is an implementation of the SHA-1 (Secure Hash Algorithm 1) cryptographic hash function in Python. The script includes a main function `sha1()` that takes an input string and returns a hash value. Additionally, the script allows comparing the speed of the `sha1()` function with Python's built-in `hashlib` library function. Unit tests are also included in the project.

## Running the Script

To run the script, simply execute the main.py file in Python:

```bash
python main.py
```
Then, you'll be prompted to enter the data to hash. Enter your data, and the script will display both the SHA-1 hash and the time it took to compute the hash using both the custom and the built-in function.

## Running the Tests
To run the unit tests, execute the tests.py file:

```bash
python -m unittest tests.py
```

This will run a series of four tests that check whether the sha1() function produces the correct hash for different input strings.

## About SHA-1
SHA-1 is a cryptographic hash function that takes an input (or 'message') and returns a fixed-size string of bytes, which is a cryptographic hash. The hash is typically rendered as a hexadecimal number, 40 digits long. However, it is known to have security vulnerabilities and is not recommended for further use. This project is intended for educational purposes.
