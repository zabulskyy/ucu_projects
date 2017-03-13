from string import ascii_uppercase as upp


class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.replace(' ', '').upper()

    @staticmethod
    def combine_character(plain, keyword):
        if keyword.upper() not in upp or plain.upper() not in upp:
            return None
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)
        
    @staticmethod
    def separate_character(cypher, keyword):
        if cypher.upper() not in upp or keyword.upper() not in upp:
            return None
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)
        
    def extend_keyword(self, num):
        result = ''
        for i in range(num):
            result += self.keyword[i % len(self.keyword)]
        return result
        
    def _code(self, text, combine_func):
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)
        
    def encode(self, plaintext):
        return self._code(plaintext, self.combine_character)
    
    def decode(self, ciphertext):
        return self._code(ciphertext, self.separate_character)

        
ex = VigenereCipher('csucu')
