# class Database:
#     def __init__(self, reservations):
#         self.reservations = reservations

#     def getReservations(self):
#         return self.reservations

#     def addReservation(self, res):
#         self.reservations.append(res)

#     def removeReservation(self, res):
#         self.reservations.pop(res)



# class Table:
#     def __init__(self, Tnumber, Maxseats):
#         self.Tnumber = Tnumber
#         self.Maxseats = Maxseats
    

class Reservation:
    def __init__(self, name, number, table):
        self.name = name 
        self.number = number
        self.table = table
    
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number
    
    def getTable(self):
        return self.table
    

def getFreeTables(tables, dataset):
    fullTables = set()
    for elem in dataset:
        if elem.getTable() in tables:
            fullTables.add(elem.getTable())
    freeTables = tables.difference(fullTables)
    return freeTables
    

