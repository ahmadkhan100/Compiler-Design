class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, identifier):
        if identifier in self.table:
            raise Exception(f"Variable {identifier} already declared.")
        self.table[identifier] = None

    def lookup(self, identifier):
        if identifier not in self.table:
            raise Exception(f"Variable {identifier} not declared.")
        return self.table[identifier]

    def update(self, identifier, value):
        if identifier not in self.table:
            raise Exception(f"Variable {identifier} not declared.")
        self.table[identifier] = value

symbol_table = SymbolTable()
