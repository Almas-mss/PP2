class TameImpala:

    def __init__(self, smthg):
        self.name = smthg

    def getstring(self):
        self.name = input("Enter something: ")

    def printstring(self):
        print(self.name.upper())

a1 = TameImpala("")
a1.getstring()
a1.printstring()