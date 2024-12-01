from hash_table import HashTable


class SymbolTableIdentifiersConstants:
    """
    Symbol Table for storing identifiers and constants using a HashTable.

    Methods:
        add_constant: Adds a constant to the symbol table.
        get_constant: Retrieves a constant's position from the symbol table.
        add_identifier: Adds an identifier to the symbol table.
        get_identifier_value: Retrieves an identifier's position from the symbol table.
    """

    def __init__(self):
        self.symboltable = HashTable()

    def add_constant(self, identifier):
        self.symboltable.add(identifier)

    def get_constant(self, identifier):
        return self.symboltable.get(identifier)

    def add_identifier(self, identifier):
        self.symboltable.add(identifier)

    def get_identifier_value(self, identifier):
        return self.symboltable.get(identifier)


