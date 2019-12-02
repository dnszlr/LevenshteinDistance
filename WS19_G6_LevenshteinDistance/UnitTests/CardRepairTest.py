import unittest
from Card import *
from CardRepair import CardRepair

class Test_CardRepairTest(unittest.TestCase):
    def test_A(self):
        
        card1 = Card("hallooo", 2,4,5,6)
        card2 = Card("haoo", 2,4,5,6)
        card3 = Card("halloogo", 2,4,5,6)
        card4 = Card("hallooffrfo", 2,4,5,6)
        list1 = [card2, card3, card4]
        cardRepair1 = CardRepair(card1, list1)#
        assert(cardRepair1.LD(list1[1]) is not None)
        assert(card1 is not None)
       # self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()