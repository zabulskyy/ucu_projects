class Ship:
    def __init__(self, length, field):
        """
        :param length: int
        :param field: dict <tuple <int,int> : str>
        """
        self.field = field
        __data = self.create_ship(length)
        self.bow = __data[0]
        self.horizontal = __data[1]
        self._length = length
        _hit = []
        for i in range(length):
            _hit.append('*')
        self._hit = _hit

    def create_ship(self, length):
        """
        :param length: int
        :return: tuple <int,int>, bool
        """
        field = self.field
        from random import choice
        stars = []
        for i in field:
            if field[i] == '*':
                stars.append(i)
        fail = True
        while fail:
            fail = False
            horizontal = choice([True, False])
            if horizontal:
                bow = (choice([i[0] for i in field]),
                       choice([i[1] for i in field if i[1] < 10 - length]))
                for i in range(-1, 2):
                    for j in range(-1, length + 1):
                        if (bow[0] + i, bow[1] + j) in stars:
                            fail = True
            else:
                bow = (choice([i[0] for i in field if i[0] < 10 - length]),
                       choice([i[1] for i in field]))
                for i in range(-1, 2):
                    for j in range(-1, length + 1):
                        if (bow[0] + j, bow[1] + i) in stars:
                            fail = True
        return bow, horizontal


class Field:
    def __init__(self):
        self.field = {}
        for i in range(10):
            for j in range(10):
                self.field[(i, j)] = ' '

        list_field = []
        a = []
        for i in range(10):
            for j in range(10):
                a.append(' ')
            list_field.append(a)
            a = []
        del (a)

        for i in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
            temp = Ship(i, self.field)
            if temp.horizontal:
                for j in range(temp._length):
                    self.field[(temp.bow[0], temp.bow[1] + j)] = '*'
            else:
                for j in range(temp._length):
                    self.field[(temp.bow[0] + j, temp.bow[1])] = '*'

        for j in self.field:
            list_field[j[0]][j[1]] = self.field[j]
        self.field = list_field

    def shoot_at(self, tuple):
        field = self.field
        x = tuple[1] - 1
        y = tuple[0] - 1
        if field[y][x] == '*' or field[y][x] == 'X':
            field[y][x] = 'X'
        elif field[y][x] == ' ' or field[y][x] == 'O':
            field[y][x] = 'O'

    def field_without_ships(self):
        field = self.field
        semi_field = []
        a = []
        for i in range(10):
            for j in range(10):
                a.append(' ')
            semi_field.append(a)
            a = []
        for i in range(10):
            for j in range(10):
                if field[i][j] == 'O':
                    semi_field[i][j] = 'O'
                elif field[i][j] == 'X':
                    semi_field[i][j] = 'X'
        return semi_field

    def field_with_ships(self):
        return self.field

    def check_ship(self, tuple):
        field = self.field
        x = tuple[1] - 1
        y = tuple[0] - 1
        if field[y][x] == '*' or field[y][x] == 'X':
            return 1
        elif field[y][x] == ' ' or field[y][x] == 'O':
            return 0


class Player:
    def __init__(self):
        self._name, self.pw, self.permission = self.log()
        self.score = 0
        
    def decrypt(self, word):
        from string import ascii_lowercase as low, ascii_uppercase as upp
        from random import choice
        
        d_word = ''
        for i in word:
            d_word += i
            for j in range(9):
                d_word += choice(upp + low)
        return d_word
        
    def encrypt(self, word):
        d_word = [word[i] for i in range(0, len(word), 10)]
        solved = ''
        for i in d_word:
            solved += i
        return solved
    
    def verify(self, user, pw):
        from pass_list import u_p
        for i in u_p:
            if (i, self.encrypt(u_p[i][0])) == (user, pw):
                return True
        return False

    def read_position(self, target):
        from string import ascii_lowercase as lett
        lett = lett[:10]
        target = target.lower()
        return lett.index(target[0]) + 1, int(target[1:])

    def log(self):
        from pass_list import u_p
        names = list(u_p)
        pw = ''
        while not pw:
            name = input('Hello, Player, please, type your name: ')
            if name in names:
                pw = input('Hi, {0}, please, type your password. Leave line empty if it\'s not you: '.format(name))
                if not self.verify(name, pw):
                    print('Name or password is invalid')
                    pw = ''
            else:
                pw = input('Oh, {0}, you are new here. Please choose your password (be sure it is longer than 3): '.format(name))
                if len(pw) < 3:
                    pw = ''    
        if name not in u_p:
            u_p[name] = [self.decrypt(pw), 0, 0]
        return (name, pw, u_p[name][2])        
            

class Game:
    def __init__(self):
        from pass_list import u_p
        self.indx = 0
        f1 = Field()
        f2 = Field()
        
        p1 = Player()
        p2 = Player()

        self.fields = [f1, f2]
        self.players = [p1, p2]

        player = self.players[self.indx]
        self.current_player = player
        
    def read_position(self, target):
        return self.players[self.indx].read_position(target)

    def field_without_ships(self):
        return self.fields[self.indx].field_without_ships()

    def field_with_ships(self):
        return self.fields[self.indx - 1].field_with_ships()

    def declare_winner(self):
        fir = self.fields[0].field
        sec = self.fields[1].field

        stars1 = 0
        stars2 = 0
        for i in fir:
            for j in i:
                if j == '*':
                    stars1 += 1
        for i in sec:
            for j in i:
                if j == '*':
                    stars2 += 1

        if stars1 == 0:
            return 1
        elif stars2 == 0:
            return 2
        else:
            return 0
            
    
if __name__ == "__main__":
    from random import choice as ch
    from os import system as sys
    from pass_list import u_p

    game = Game()
    sys('cls')
    game.indx = ch([1, 0])
    enemy = 0
    lett = 'ABCDEFGHIJ'
    win_cheat = 0
    while not game.declare_winner() or win_cheat:
        if game.indx == 0:
            game.indx = 1
        else:
            game.indx = 0

        input(game.players[game.indx]._name + ', your turn, are you ready?')
        sys('cls')
        print('it\'s your turn, ' + game.players[game.indx]._name)
        print('your field: \n')
        print(' 12345678910')
        for i in range(len(game.field_with_ships())):
            print(lett[i], end='', sep='')
            for j in game.field_with_ships()[i]:
                print(j, end='', sep='')
            print('\n', end='', sep='')

        print('\nyour enemy\'s field: \n')
        print(' 12345678910')
        for i in range(len(game.field_without_ships())):
            print(lett[i], end='', sep='')
            for j in game.field_without_ships()[i]:
                print(j, end='', sep='')
            print('\n', end='', sep='')
        try:
            target = input('choose target to shoot '
                           '(like {1}{0} or {3}{2}): '
                           ''.format(ch([i for i in range(1, 11)]),
                                     ch(lett).upper(),
                                     ch([i for i in range(1, 11)]),
                                     ch(lett).upper()))
                        
            #cheat: win
            if target == 'cheat: win' and game.players[game.indx].permission:
                win_cheat = 1
                break
                
            #cheat: show field
            if target == 'cheat: show field' and game.players[game.indx].permission:
            
                if game.indx == 0:
                    game.indx = 1
                else:
                    game.indx = 0
                    
                print('\nyour enemy\'s field (hacked): \n')
                print(' 12345678910')
                for i in range(len(game.field_with_ships())):
                    print(lett[i], end='', sep='')
                    for j in game.field_with_ships()[i]:
                        print(j, end='', sep='')
                    print('\n', end='', sep='')
                        
                if game.indx == 0:
                    game.indx = 1
                else:
                    game.indx = 0
                    
                target = input('choose target to shoot '
                               '(like {1}{0} or {3}{2}): '
                               ''.format(ch([i for i in range(1, 11)]),
                                         ch(lett).upper(),
                                         ch([i for i in range(1, 11)]),
                                         ch(lett).upper()))
                                         
            target = game.read_position(target)
            game.fields[game.indx].shoot_at(target)
            if game.fields[game.indx].check_ship(target):
                input('BAM!')
                if game.indx == 1:
                    game.indx = 0
                else:
                    game.indx = 1
            else:
                input('missshoot')
        except:
            input('your input was invalid, skip your turn!!')
        sys('cls')

    sys('cls')
    if not win_cheat:
        index = game.declare_winner() - 1
        print('Gratz, {0}, you win!, Your score: {1}'.format(game.players[index]._name, u_p[game.players[index]._name][1]))
    else:
        print('Gratz, admin, you win! Your score: over 9000')
