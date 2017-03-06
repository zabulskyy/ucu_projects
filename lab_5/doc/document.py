class CursorOutOfFileForward(Exception):
    pass


class CursorOutOfFileBack(Exception):
    pass


class InvalidDelete(Exception):
    pass


class InvalidSave(Exception):
    pass


class InvalidCharacter(Exception):
    pass


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0
        
    def forward(self):
        """move cursor 1 character forward"""
        if self.position > len(self.document.string) - 1:
            raise CursorOutOfFileForward("Cursor out of file")
        self.position += 1

    def back(self):
        """move cursor 1 character back"""
        if self.position == 0:
            raise CursorOutOfFileBack("Cursor out of file")
        self.position -= 1
        
    def home(self):
        """move cursor forward to the closest newline"""
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """move cursor back to the closest newline"""
        while self.position < len(
            self.document.characters) and \
            self.document.characters[
                    self.position
                    ].character != '\n':
            self.position += 1


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def set_name(self, message=''):
        self.filename = input(message)

    def insert(self, character):
        """type character to the cursor position"""
        if len(character) - 1:
            raise InvalidCharacter('Can not add more that one character per once')
        self.characters.insert(self.cursor.position,
                               character)
        self.cursor.forward()
        
    def delete(self):
        """delete character after cursor"""
        if self.cursor.position > len(self.string) - 1:
            raise InvalidDelete("Can not delete character on this position")
        del self.characters[self.cursor.position]
    
    def save(self):
        """save document"""
        if not self.filename:
            raise InvalidSave("Can not save file without name")
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        """show document as string"""
        return "".join((str(c) for c in self.characters))


class Character:
    def __init__(self, character, bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline
        
    def __str__(self):
        """add decorator ('*', '/' or '_') due to text style"""
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

    def insert(self, character):
        """if character don't have atribute 'character' - add it'"""
        if not hasattr(character, 'character'):
            self.character = Character(character)
