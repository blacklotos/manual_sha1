import unittest
import binascii
from main import sha1

class TestSha1(unittest.TestCase):
    def test_sha1_short(self):
        data = "Hello, world!"
        expected = "943a702d06f34599aee1f8da8ef9f7296031d699"
        self.assertEqual(binascii.hexlify(sha1(data.encode('utf-8'))).decode(), expected)

    def test_sha1_empty_string(self):
        data = ""
        expected = "da39a3ee5e6b4b0d3255bfef95601890afd80709"
        self.assertEqual(binascii.hexlify(sha1(data.encode('utf-8'))).decode(), expected)

    def test_sha1_long(self):
        data = "The quick brown fox jumps over the lazy cog The quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dog"
        expected = "ea09b05991599a70b78778e5f895c5f517987442"
        self.assertEqual(binascii.hexlify(sha1(data.encode('utf-8'))).decode(), expected)


if __name__ == '__main__':
    unittest.main()
