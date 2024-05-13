import enum
from collections import namedtuple




class Player(enum.Enum): #플레이어 (enum을 활용해 상수에 이름을 붙여 플레이어로 사용하도록 한다.)
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
    
class Point(namedtuple('Point', 'row col')): #바둑판 상에서의 돌의 좌표
    def neighbors(self):
        return [
            Point(self.row-1, self.col),
            Point(self.row+1, self.col),
            Point(self.row, self.col-1),
            Point(self.row, self.col+1)
        ]
            