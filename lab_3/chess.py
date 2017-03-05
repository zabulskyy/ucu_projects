"""aggregation"""
class A_Board():
    def __init__(self):
        from string import ascii_uppercase as lett
        self._size = (8, 8)
        coords ={}
        for i in range(1, 9):
            for j in lett:
                coords[(j+str(i))] = None
        self.coords = coords
        
class A_Piece():
    def __init__(self, type, color, coords):
        self.type = type
        self.color = color
        self.coords = coords
        
    def put_piece_on_board(self, board):
        board.coords[coords] = (self.color, self.type)



"""composition"""
class C_Board():
    def __init__(self):
        from string import ascii_uppercase as lett
        self._size = (8, 8)
        coords ={}
        for i in range(1, 9):
            for j in lett:
                coords[(j+str(i))] = None
        self.coords = coords
        
    def create_and_put(self):
        black_horse_1 = C_Piece('black', 'horse')
        self.coords['A2'] = (black_horse_1.color, black_horse_1.type)
        
class C_Piece():
    def __init__(self, color, type):
        self.type = type
        self.color = color
        
