
"""
pion

cavalier
fou
tour
dame
roi

blanc / noir

position A..H 1..8

place piece @ position
"""

letterToNumber = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
numberToLetter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class CaseVide:
    pass

chess = [
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()],
    [CaseVide(), CaseVide(), CaseVide(), CaseVide(),CaseVide(), CaseVide(),CaseVide(), CaseVide()]
]

caseVide = 0
pion = 1
pionBlanc = 1
pionNoir = 11

chess2 = [ [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

class Piece:
    def __init__(self, color):
        print("cons Piece")
        self.color = color

    def place(self, h, v):
        self.h = h
        self.v = v

    def getColor(self):
        return self.color

class PieceBlanche(Piece):
    def __init__(self):
        print("cons PieceBlanche")
        Piece.__init__(self, 'blanc')

class PieceNoire(Piece):
    def __init__(self):
        print("cons PieceNoire")
        Piece.__init__(self, 'noir')

class Pion(Piece):
    def __init__(self):
        print("cons Pion")

class PionBlanc(Pion, PieceBlanche):
    def __init__(self):
        print("cons PionNoir")
        Pion.__init__(self)
        PieceBlanche.__init__(self)
        #self.color = 'blanc'

    def getMoves(self):
        moves = []
        if self.v < 7:
            if self.h > 0:
                x = whatPos(self.h-1, self.v+1)
                if isinstance(x, PieceNoire):
                    moves.append((self.h-1, self.v+1))
            if self.h < 7:
                x = whatPos(self.h+1, self.v+1)
                if isinstance(x,PieceNoire):
                    moves.append((self.h+1, self.v+1))
            x = whatPos(self.h, self.v+1)
            if isinstance(x, CaseVide):
                moves.append((self.h, self.v+1))

        return moves

class PionNoir(Pion, PieceNoire):
    def __init__(self):
        print("cons PionNoir")
        Pion.__init__(self)
        PieceNoire.__init__(self)

    def getMoves(self):
        moves = []
        if self.v > 1:
            if self.h > 0:
                x = whatPos(self.h-1, self.v-1)
                if isinstance(x, PieceBlanche):
                    moves.append((self.h-1, self.v-1))
            if self.h < 7:
                x = whatPos(self.h+1, self.v-1)
                if isinstance(x,PieceBlanche):
                    moves.append((self.h+1, self.v-1))
            x = whatPos(self.h, self.v-1)
            if isinstance(x, CaseVide):
                moves.append((self.h, self.v-1))

        return moves

class Cavalier(Piece):
    def __init__(self):
        pass

    def getMoves(self):
        moves = []
        x = whatPos(self.h-2, self.v+1)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h-2, self.v+1))
        x = whatPos(self.h-1, self.v+2)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h-1, self.v+2))
        x = whatPos(self.h+1, self.v+2)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h+1, self.v+2))
        x = whatPos(self.h+2, self.v+1)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h+2, self.v+1))
        x = whatPos(self.h+2, self.v-1)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h+2, self.v-1))
        x = whatPos(self.h+1, self.v-2)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h+1, self.v-2))
        x = whatPos(self.h-1, self.v-2)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h-1, self.v-2))
        x = whatPos(self.h-2, self.v-1)
        if isinstance(x,self.adverse) or isinstance(x,CaseVide):
            moves.append((self.h-2, self.v-1))

        return moves

    def setAdverse(self, adverse):
        self.adverse = adverse

class CavalierBlanc(Cavalier, PieceBlanche):
    def __init__(self):
        Cavalier.__init__(self)
        PieceBlanche.__init__(self)
        Cavalier.setAdverse(self, PieceNoire)

class CavalierNoir(Cavalier, PieceNoire):
    def __init__(self):
        Cavalier.__init__(self)
        PieceNoire.__init__(self)
        Cavalier.setAdverse(self, PieceBlanche)


def place(piece, norm):
    pos = normToPos(norm)
    chess[pos[0]][pos[1]] = piece
    piece.place(pos[0], pos[1])

def getMoves(piece):
    mymoves = []
    moves = piece.getMoves()
    for m in moves:
        mymoves.append(posToNorm(m))
    return mymoves

def normToPos(norm):
    return (letterToNumber[norm[0]]-1, int(norm[1])-1)

def posToNorm(pos):
    return numberToLetter[pos[0]] + str(pos[1]+1)

def whatPos(x,y):
    if x<0 or x>7:
        return None
    if y<0 or y>7:
        return None
    return chess[x][y]

def whatsHere(norm):
    pos = normToPos(norm)
    return chess[pos[0]][pos[1]]



#place(Pion('blanc'), 'A2')
pb1 = PionBlanc()
pb2 = PionBlanc()
pb3 = PionBlanc()
pb4 = PionBlanc()
pb5 = PionBlanc()
pb6 = PionBlanc()
pb7 = PionBlanc()
pb8 = PionBlanc()
pn1 = PionNoir()
pn2 = PionNoir()
pn3 = PionNoir()
pn4 = PionNoir()
pn5 = PionNoir()
pn6 = PionNoir()
pn7 = PionNoir()
pn8 = PionNoir()
place(pb1,'A2')
place(pb2,'B2')
place(pb3,'C2')
place(pb4,'D2')
place(pb5,'E2')
place(pb6,'F2')
place(pb7,'G2')
place(pb8,'H2')
place(pn1,'A7')
place(pn2,'B7')
place(pn3,'C7')
place(pn4,'D7')
place(pn5,'E7')
place(pn6,'F7')
place(pn7,'G7')
place(pn8,'H8')
cb1 = CavalierBlanc()
cb2 = CavalierBlanc()
cn1 = CavalierNoir()
cn2 = CavalierNoir()
place(cb1,'B1')
place(cb2,'G1')
place(cn1,'B8')
place(cn2,'G8')
m = getMoves(cn1)
print(m)
print(cn1.getColor())


