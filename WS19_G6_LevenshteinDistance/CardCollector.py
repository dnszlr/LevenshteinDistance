import os
from Card import Card
from CardRepair import CardRepair

class CardCollector(object):
    
    #List brokenCards to save the broken Cards in a List
    #List referenceNames to save the correct Names in a List
    #List repairedCards to safe the repaird Cards in a List
    #Class attributes
    def __init__(self):
        self.brokenCards = []
        self.referenceNames = []
        self.repairedCards = []

    #Builds cards from the parameter filename and writes them into self.brokenCards.
    #Parameters:
    #Opens a file from the parameter filename
    def buildScrambled(self, filename):

        #Preconditon
        assert(filename != None) 
        assert(len(self.brokenCards) == 0)

        relPath = "Files/" + filename + ".txt"
        file = open(relPath, "r+")      

        for line in file:
            lineSplit = line.split("|") #Splitting the scrambled card String on "|"
            brokenCard = Card(lineSplit[0], lineSplit[1], lineSplit[2], lineSplit[3], lineSplit[4])
            self.brokenCards.append(brokenCard)

        file.close()  

        #Postcondition
        assert(file.closed) 
        assert(len(self.brokenCards) > 0)

    #Reads strings from the parameter filename and writes them into self.referenceNames.
    #Parameters:
    #Opens the relative path from the parameter file
    def buildReference(self, filename):
        #Precondition
        assert(filename != None) 
        assert(len(self.referenceNames) == 0)

        relPath = "Files/" + filename + ".txt"
        file = open(relPath, "r+")   #open the file with relPath

        for line in file:
            #reading file and convert into string line by line 
            #-1 because in file is at the end of string a \n to end the line
            self.referenceNames.append(str(line[:-1])) 

        file.close()                #close the file

        #Postcondition
        assert(file.closed)
        assert(len(self.referenceNames) > 0)

    #Writes the repairedCards into a selected path
    #Parameters:
    #path - create a new file at the given path
    def writeFile(self, path):
        assert(path != None) #Precondition
        assert(len(self.repairedCards) > 0) #Precondition

        file = open("Files/" + path + ".txt", "w+")
        for fixedCard in self.repairedCards:        #getting all parameter from card and write it in the new file
            cardString = fixedCard.name + "|" + fixedCard.mana + "|" + fixedCard.cmc + "|" + fixedCard.type + "|" + fixedCard.count
            file.write(cardString)
        file.close()

        assert(file.closed) #Postcondition

    #go through the broken Card List with for each loop. calling repair method with a cardRepairObject
    def getRepairedCardsList(self):
        assert(len(self.repairedCards) == 0) #Precondition
        for brokenCard in self.brokenCards:
            brokenCardName = brokenCard.name
            cardRepairObject = CardRepair(brokenCard, self.referenceNames)
            cardRepairObject.repair()
            self.repairedCards.append(cardRepairObject.card)

        assert(len(self.repairedCards) > 0) #Postcondition

    #repairing the card on index i and return it
    def getRepairedCard(self, i):
        assert(i >= 0) #Precondition
        cardRepairObject = CardRepair(self.brokenCards[i], self.referenceNames)
        card = cardRepairObject.repair()
        assert(card != None) #Postconditon
        return card