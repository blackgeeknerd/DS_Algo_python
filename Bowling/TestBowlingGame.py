import unittest
from Bowling.BowlingGame import BowlingGame
import BowlingGame as bg

class TestBowlingGame(unittest.TestCase):
    
    # def testCreateGame(self):
    #     game = bg.BowlingGame()
        
    def setup(self):
        self.game = bg.BowlingGame()
        
    def testGutterGame(self):
        # for i in range(20):
        #     self.game.roll(0)
        self.rollMany(0, 20)
        assert self.game.score() == 0
        
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20
        
        
    def testOneSpare(self):
         self.game.roll(5)
         self.game.roll(5)
         self.game.roll(3)
         self.rollMany(0, 17)
         assert self.game.score == 16
         
         
    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24
        
    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300
        
        
    def testAllSpares(self):
        self.rollMany(5,21)
        assert self.game.score() == 150
        
        
    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
            
        