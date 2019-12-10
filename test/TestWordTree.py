import unittest

from src.WTNode import WTNode
from src.WordTree import WordTree


class TestAddToWordTree(unittest.TestCase):

    def test_empty_word_tree(self):
        wordTree = WordTree()
        self.assertEqual(str(wordTree), 'None')

    def test_add_single_word(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        expected_result = "(c, 0) -> [None, (a, 0) -> [None, (r, 1) -> [None, None, None], None], None]"
        self.assertEqual(str(wordTree), expected_result)

    def test_add_two_similar_words(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "cat")
        expected_result = "(c, 0) -> [None, (a, 0) -> [None, (r, 1) -> [None, None, (t, 1) -> [None, None, None]], None], None]"
        self.assertEqual(str(wordTree), expected_result)

    def test_add_word_to_left_of_root(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "as")
        expected_result = "(c, 0) -> [(a, 0) -> [None, (s, 1) -> [None, None, None], None], (a, 0) -> [None, (r, 1) -> [None, None, None], None], None]"
        self.assertEqual(str(wordTree), expected_result)

    def test_add_word_to_right_of_root(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "space")
        expected_result = "(c, 0) -> [None, (a, 0) -> [None, (r, 1) -> [None, None, None], None], (s, 0) -> [None, (p, 0) -> [None, (a, 0) -> [None, (c, 0) -> [None, (e, 1) -> [None, None, None], None], None], None], None]]"
        self.assertEqual(str(wordTree), expected_result)

    def test_multiple_word_tree_size(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "space")
        wordTree.add(word = "sake")
        self.assertEqual(wordTree.size, 3)

    def test_add_multiple_of_same_word(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "car")
        wordTree.add(word = "car")
        self.assertEqual(wordTree.size, 3)
        expected_result = "(c, 0) -> [None, (a, 0) -> [None, (r, 3) -> [None, None, None], None], None]"
        self.assertEqual(str(wordTree), expected_result)

    def test_append_node_to_parent_node_no_existing_siblings(self):
        parent_node = WTNode('c', None, None, None)
        wordTree = WordTree()

        wordTree.append_node_to_parent_node(parent_node, 'a')
        expected_result = "(c, 0) -> [(a, 0) -> [None, None, None], None, None]"
        self.assertEqual(str(parent_node), expected_result)

    def test_append_node_to_parent_node_with_existing_siblings(self):
        parent_node = WTNode('c', WTNode('a'), None, WTNode('d'))
        wordTree = WordTree()

        wordTree.append_node_to_parent_node(parent_node, 'g')
        expected_result = "(c, 0) -> [(a, 0) -> [None, None, None], None, (d, 0) -> [None, None, (g, 0) -> [None, None, None]]]"
        self.assertEqual(str(parent_node), expected_result)

    def test_append_node_to_parent_node_same_character(self):
        parent_node = WTNode('c', None, None, WTNode('d'))
        wordTree = WordTree()

        wordTree.append_node_to_parent_node(parent_node, 'c')
        expected_result = "(c, 0) -> [None, None, (d, 0) -> [None, None, None]]"
        self.assertEqual(str(parent_node), expected_result)

class TestCountWordTree(unittest.TestCase):
    def test_count_word_added_once(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "space")
        result = wordTree.count("car")
        self.assertEqual(result, 1)

    def test_count_word_added_multiple_times(self):
        wordTree = WordTree()
        wordTree.add(word = "car")
        wordTree.add(word = "car")
        wordTree.add(word = "car")
        result = wordTree.count("car")
        self.assertEqual(result, 3)

    def test_count_non_existing_word_in_empty_tree(self):
        wordTree = WordTree()
        result = wordTree.count("car")
        self.assertEqual(result, None)

    def test_count_non_existing_word_in_populated_tree(self):
        wordTree = WordTree()
        wordTree.add(word = "hey")
        result = wordTree.count("car")
        self.assertEqual(result, None)

    def test_count_empty_string(self):
        wordTree = WordTree()
        wordTree.add(word = "Word")
        result = wordTree.count("")
        self.assertEqual(result, None)

class TestMinstWordTree(unittest.TestCase):
    def test_minst_with_empty_tree(self):
        wordTree = WordTree()
        result = wordTree.minst()
        self.assertEqual(None, result)

    def test_minst_with_single_word_in_tree(self):
        wordTree = WordTree()
        wordTree.add("car")
        result = wordTree.minst()
        self.assertEqual("car", result)

    def test_minst_with_single_character_word(self):
        wordTree = WordTree()
        wordTree.add("car")
        wordTree.add("b")
        result = wordTree.minst()
        self.assertEqual("b", result)

    def test_minst_with_multiple_same_word(self):
        wordTree = WordTree()
        wordTree.add("car")
        wordTree.add("car")
        result = wordTree.minst()
        self.assertEqual("car", result)

class TestWordTreeNode(unittest.TestCase):

    def test_new_word_tree_node(self):
        node = WTNode('A')
        self.assertEqual(node.multiplicity, 0)
        self.assertEqual(node.character, 'A')

    def test_new_word_tree_node_with_child_node(self):
        childNode = WTNode('C')
        parentNode = WTNode(character = 'C', middle = childNode)
        self.assertEqual(parentNode.middle, childNode)

    def test_increase_multiplicity_by_default_value(self):
        node = WTNode('A')
        self.assertEqual(node.multiplicity, 0)

        node.increase_multiplicity()
        self.assertEqual(node.multiplicity, 1)

    def test_increase_multiplicity_by_custom_value(self):
        node = WTNode('A')
        self.assertEqual(node.multiplicity, 0)

        node.increase_multiplicity(increase = 3)
        self.assertEqual(node.multiplicity, 3)



if __name__ == '__main__':
    unittest.main()