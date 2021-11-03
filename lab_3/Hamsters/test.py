import unittest

from Hamsters.Hamster import hamster


class TestQuickSort(unittest.TestCase):
    def test_hamster(self):
        S = 7
        C = 3
        infoHamsters = [[1, 2], [2, 2], [3, 1]]  # [H G]

        self.assertEqual(hamster(infoHamsters, S, C), 2)

    def test_hamster2(self):
        S = 19  # Кількість пакетів у покупця

        C = 4  # Кількість хомяків в магазині
        infoHamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]  # [H-денна норма для хомяка G-жадібність за кожного сусіда]

        self.assertEqual(hamster(infoHamsters, S, C), 3)

    def test_hamster3(self):
        S = 10
        C = 10
        infoHamsters = [[1, 1], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]  # [H G]

        self.assertEqual(hamster(infoHamsters, S, C), 9)

    def test_hamster4(self):
        S = 2
        C = 2
        infoHamsters = [[1, 22222], [1, 222222], ]  # [H G]

        self.assertEqual(hamster(infoHamsters, S, C), 1)