
class Card(object):

    #Name, Mana, CMC, Type, Count Attributes of every Card
    #Class Constructor
    def __init__(self, name, mana, cmc, type, count):
        self.name = name
        self.mana = mana
        self.cmc = cmc
        self.type = type
        self.count = count

    #Inserts the letter c at the index i
    def insert(self, i, c):
        assert(i >= 0) #Precondition

        self.name = self.name[:i] + c + self.name[i:]

        assert(self.name[i] == c) #Postcondition

    #Deletes the letter at the index i
    def delete(self, i):
        assert(i >= 0) #Precondition

        lenOld = len(self.name)
        self.name = self.name[0 : i :] + self.name[i + 1 : :]

        assert(len(self.name) < lenOld) #Postcondition 

    #Replaces the letter at index i with c.
    def replace(self, i, c):
        assert(i >= 0) #Precondition

        self.name = self.name[:i] + c + self.name[i + 1:]

        assert(self.name[i] == c) #Postcondition