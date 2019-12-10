class WTNode:
    def __init__(self, character = '', left = None, middle = None, right = None):
        self.character = character
        self.left = left
        self.middle = middle
        self.right = right
        self.multiplicity = 0

    def increase_multiplicity(self, increase = 1):
        self.multiplicity = self.multiplicity + increase

    def __str__(self):
        st = "(" + str(self.character) + ", " + str(self.multiplicity) + ") -> ["
        st += str(self.left) if self.left is not None else "None"
        st += ", " + str(self.middle) if self.middle is not None else ", None"
        st += ", " + str(self.right) if self.right is not None else ", None"
        return st + "]"
