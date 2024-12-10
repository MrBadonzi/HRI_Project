class Database:
    def __init__(self):
        self.database = [Reservation("Mario", 3, 1), Reservation("Jacob", 4, 2), Reservation("Dan", 2, 3),
            Reservation("Bob", 3, 4),
            Reservation("Sara", 4, 5), Reservation("Sandy", 2, 6)]

    def getDatabase(self):
        return self.database

class Table:
    def __init__(self):
        self.tables = {1, 2, 3, 4, 5, 6, 7}

    def getTables(self):
        return self.tables


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
