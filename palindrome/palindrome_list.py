from linkedstack import LinkedStack


class Palindrome:
    def __init__(self):
        self.words = []

    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            for word in file.readlines():
                word = word.split()[0]
                self.words.append(word)

    @staticmethod
    def is_palindrome(word):
        stack = LinkedStack()
        for index in range(len(word) // 2):
            stack.push(word[index])
        for index in range((len(word) + 1) // 2, len(word)):
            if stack.peek() == word[index]:
                stack.pop()
            else:
                return False
        return True

    def write_pali(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for word in self.words:
                if Palindrome.is_palindrome(word):
                    file.write(word + "\n")

a = Palindrome()
a.read("base.lst")
a.write_pali("result.txt")

