import unittest
from heap_sort import heap_sort

class TestHeapSort(unittest.TestCase):

    # def test_add(self):
    #     self.assertEqual(2+2, 5)
    # # cmd doesn't see first test(even if it obviously false)
    # # and I don't know why, so I added this

    def test_desc_to_asc(self):
        arr = [6, 5, 4, 3, 2, 1]
        heap_sort(arr, "asc")
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])

    def test_asc_to_desc(self):
        arr = [1, 2, 3, 4, 5, 6]
        heap_sort(arr, "desc")
        self.assertEqual(arr, [6, 5, 4, 3, 2, 1])

    def test_asc_to_desc(self):
        arr = [1, 2, 3, 4, 5, 6]
        heap_sort(arr, "desc")
        self.assertEqual(arr, [6, 5, 4, 3, 2, 1])

    def test_desc_to_desc(self):
        arr = [6, 5, 4, 3, 2, 1]
        heap_sort(arr, "desc")
        self.assertEqual(arr, [6, 5, 4, 3, 2, 1])

    def test_sort_1(self):
        arr = [5, 4, 6, 1, 2, 3]
        heap_sort(arr, "asc")
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()