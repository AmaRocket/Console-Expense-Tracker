#from expense import Expense

class Expense():
    favs = [] #class

    def __init__(self, title, cost):
        self.title = title
        self.cost = cost

    def is_short(self):
        if self.cost < 100:
            return true

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.cost} dollars"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.cost == other.cost):
            return True
    
    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()