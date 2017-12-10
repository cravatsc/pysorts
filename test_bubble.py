import unittest
import bubble


class MyTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        list = [5,4,3,2,1]
        bubble.bubble(list)
        self.assertEqual(list, [1,2,3,4,5])


    def test_swap(self):
        list = [2, 3]
        bubble.swap(list, 0, 1)
        self.assertEqual(list, [3,2])


if __name__ == '__main__':
    unittest.main()
