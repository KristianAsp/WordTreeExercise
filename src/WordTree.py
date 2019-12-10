from src.WTNode import WTNode


class WordTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def set_root(self, node = None):
        self.root = node

    def add(self, word = ""):
        if word == "":
            return self.root

        self.pointer = self.root
        index = 0
        for character in word:
            if self.root is None:  # Means we have an empty WordTree
                self.root = WTNode(character, None, None, None)
                self.pointer = self.root
            else:
                if character == self.pointer.character:
                    if self.pointer.middle is None:
                        continue
                    elif index == len(word) - 1:
                        break
                    else:
                        self.pointer = self.pointer.middle
                elif self.pointer.middle is None and self.pointer.character == word[index - 1]:
                    node = WTNode(character, None, None, None)
                    self.pointer.middle = node
                    self.pointer = self.pointer.middle
                else:
                    self.pointer = self.append_node_to_parent_node(self.pointer, character)

            index += 1
        self.pointer.increase_multiplicity()
        self.size += 1

    def append_node_to_parent_node(self, pointer, character):
        if character > pointer.character:
            if pointer.right is not None:
                return self.append_node_to_parent_node(pointer.right, character)
            else:
                pointer.right = WTNode(character, None, None, None)
                return pointer.right
        elif character < pointer.character:
            if pointer.left is not None:
                return self.append_node_to_parent_node(pointer.left, character)
            else:
                pointer.left = WTNode(character, None, None, None)
                return pointer.left
        else:
            return pointer

    def increase_size(self):
        self.size = self.size + 1

    def count(self, word = ""):
        if word == "" or self.root is None:
            return None

        pointer = self.root
        while len(word) != 0:
            character = word[0]
            if pointer.character == character and len(word) == 1:
                return pointer.multiplicity
            elif pointer.character == character:
                pointer = pointer.middle
                word = word[1:]
            elif character > pointer.character and pointer.right is not None:
                pointer = pointer.right
            elif character < pointer.character and pointer.left is not None:
                pointer = pointer.left
            else:
                return None


    # Find lexicographically smallest word in tree
    def minst(self):
        if self.root is None:
            return None

        pointer = self.root
        constructed_word = ""

        while True:
            if pointer.left is not None:
                pointer = pointer.left
                continue
            else:
                constructed_word += pointer.character
            if pointer.multiplicity != 0:
                return constructed_word
            elif pointer.middle is not None:
                pointer = pointer.middle
            else:
                return None

    def __str__(self):
        return str(self.root)