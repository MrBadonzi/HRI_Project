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
