class SymbolTable:
    def __init__(self):
        self.global_scope = {}
        self.scopes = [self.global_scope]

    def enter_scope(self):
        """Enter a new scope (like entering a block)."""
        self.scopes.append({})

    def exit_scope(self):
        """Exit the current scope (like leaving a block)."""
        if len(self.scopes) > 1:
            self.scopes.pop()
        else:
            raise Exception("Cannot exit the global scope")

    def insert(self, identifier):
        """Insert a new identifier in the current scope."""
        current_scope = self.scopes[-1]
        if identifier in current_scope:
            raise Exception(f"Variable {identifier} already declared in the current scope.")
        current_scope[identifier] = None

    def lookup(self, identifier):
        """Lookup an identifier in all scopes, starting from the current one."""
        for scope in reversed(self.scopes):
            if identifier in scope:
                return scope[identifier]
        raise Exception(f"Variable {identifier} not declared.")

    def update(self, identifier, value):
        """Update an identifier's value in the closest scope."""
        for scope in reversed(self.scopes):
            if identifier in scope:
                scope[identifier] = value
                return
        raise Exception(f"Variable {identifier} not declared.")

symbol_table = SymbolTable()
