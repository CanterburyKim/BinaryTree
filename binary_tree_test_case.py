import unittest
from binary_tree import *

class TestBinaryTree(unittest.TestCase):
    """
    test class
    """
    def test_do_tree_insert(self):
        """
        Just testing the insert
        """
        numbers = [10, 7, 15, 12, 7, 1, 3, 33, 35]
        my_tree = Node(numbers[0])

        for number in numbers[1:]:
            my_tree.add(number)

    def test_do_tree_count(self):
        """
        """
        numbers = [10, 7, 15, 12, 7, 1, 3, 33, 35]
        my_tree = Node(numbers[0])

        for number in numbers[1:]:
            my_tree.add(number)

        count = my_tree.size()
        expected_result = len(numbers)
        self.assertEqual(count, expected_result)

    def test_do_tree_print(self):
        """
        """
        numbers = [10, 7, 15, 12, 7, 1, 3, 33, 35]
        my_tree = Node(numbers[0])

        for number in numbers[1:]:
            my_tree.add(number)
        my_tree.print()

    def test_do_tree_contains(self):
        """
        """
        numbers = [10, 7, 15, 12, 7, 1, 3, 33, 35]
        my_tree = Node(numbers[0])

        for number in numbers[1:]:
            my_tree.add(number)

        self.assertEqual(True, my_tree.contains(10))
        self.assertEqual(True, my_tree.contains(1))
        self.assertEqual(True, my_tree.contains(33))
        self.assertEqual(True, my_tree.contains(35))
        self.assertEqual(False, my_tree.contains(2))


if __name__ == '__main__':
    unittest.main()
