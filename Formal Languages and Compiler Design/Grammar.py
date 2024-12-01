class Grammar:
    # Initializes the grammar with non-terminals (N), terminals (E), start symbol (S), and productions (P).
    def __init__(self, N, E, S, P):
        self.N = N  # Non-terminals
        self.E = E  # Terminals
        self.S = S  # Start symbol
        self.P = P  # Productions (dictionary: lhs -> list of rhs lists)

    # Static method to create a grammar instance from a file.
    @staticmethod
    def from_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            # Parse non-terminals and terminals.
            N = set(Grammar.parse_line(file.readline()))
            E = set(Grammar.parse_line(file.readline()))
            # Parse start symbol (assumes line format: "S = <symbol>")
            S = file.readline().split('=')[1].replace(" ", "").strip()
            file.readline()  # Skip empty line before productions
            # Parse productions
            P = Grammar.parse_productions([line.strip() for line in file])
            # Validate the grammar
            if not Grammar.validate(N, E, S, P):
                return f"Grammar in {filename} is not valid"
            return Grammar(N, E, S, P)

    # Static method to parse a line into a list of symbols (used for N and E).
    @staticmethod
    def parse_line(line):
        return line.split('=', maxsplit=1)[1].strip().split()

    # Static method to parse production rules into a dictionary.
    @staticmethod
    def parse_productions(lines):
        P = {}
        for line in lines:
            if line == '':
                continue  # Skip empty lines
            lhs, rhs = line.split('->')  # Split into left-hand side and right-hand side
            lhs = lhs.strip()
            rhs_list = rhs.strip().split('|')  # Handle multiple RHS options
            if lhs in P:
                P[lhs].append(rhs_list)
            else:
                P[lhs] = [rhs_list]
        return P

    # Static method to validate the grammar.
    @staticmethod
    def validate(N, E, S, P):
        if S not in N:  # Start symbol must be a non-terminal
            return False
        for k, v in P.items():
            if k not in N:  # All LHS in productions must be non-terminals
                return False
            for production in v:
                for symbol in production:  # Check all symbols in RHS
                    symbol = symbol.strip().split()
                    for s in symbol:
                        if s not in N and s not in E:  # Symbols must be in N or E
                            print(s)
                            return False
        return True

    # Method to check if the grammar is context-free.
    def is_cfg(self):
        for key in self.P.keys():
            if key not in self.N:
                return False
        return True

    # Returns the productions for a given non-terminal.
    def get_nonterminal_productions(self, nonterminal):
        if nonterminal not in self.N:
            raise Exception('Can only show productions for non-terminals')
        return self.P[nonterminal]

    # Returns all non-terminals.
    def get_nonterminals(self):
        return self.N

    # Returns all terminals.
    def get_terminals(self):
        return self.E

    # String representation of the grammar.
    def __str__(self) -> str:
        return f"N = {self.get_nonterminals()}\nE = {self.get_terminals()}\nS = {self.S}\nP = {self.P}"
