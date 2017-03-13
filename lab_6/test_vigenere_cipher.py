from unittest import TestCase
from vigenere_cipher import VigenereCipher
ex = VigenereCipher('csucu')


class TestVigenereCipher(TestCase):
    def test_vigenere_cipher(self):
        self.assertEquals('A', ex.combine_character('h', 'a'), "fail")
        self.assertEquals('E', ex.combine_character('P', 'p'), "fail")
        self.assertEquals('Z', ex.combine_character('Y', 'B'), "fail")
        self.assertEquals(None, ex.combine_character('-', 'd'), "fail")
        self.assertEquals('C', ex.separate_character('a', 'y'), "fail")
        self.assertEquals(None, ex.separate_character(',', 'O'), "fail")
        self.assertEquals('H', ex.separate_character('L', 'e'), "fail")
        self.assertEquals(None, ex.separate_character('s', '!'), "fail")
        self.assertEquals('CSUCUCSUCU', ex.extend_keyword(10), "fail")
        self.assertEquals('', ex.extend_keyword(0), "fail")
        self.assertEquals('SSXYOLQGLIYBNMRGKALOTMXQORG', ex.decode('ukrainiancatholicuniversity'), "fail")
        self.assertEquals('WCLCCPAUPWCLBQFKUOPCXWLUCVQ', ex.encode('ukrainiancatholicuniversity'), "fail")
        self.assertEquals('', ex.encode(''), "fail")
        self.assertEquals('', ex.decode(''), "fail")
