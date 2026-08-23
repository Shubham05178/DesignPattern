from typing import List
import copy
class ChessPiece:
    def __init__(self,name,color,position):
        self.color=color
        self.position=position
        self.name=name
class ChessBoard:
    def __init__(self):
        self.__chesspieces=[]
    def add_pieces(self,piece):
        self.__chesspieces.append(piece)
    def display_pieces(self):
        print("ChessBoard")
        for piece in self.__chesspieces:
            print(f"{piece.color} {piece.name} is at {piece.position}")
    def clone(self):
        return copy.deepcopy(self)
p1=ChessPiece("King","White","A1")
p2=ChessPiece("King","Black","H1")
c1=ChessBoard()
c1.add_pieces(p1)
c1.add_pieces(p2)


c2=c1.clone()
c2.add_pieces(p1)
c1.display_pieces()
print("*"*20)
c2.display_pieces()