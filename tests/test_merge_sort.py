import unittest
from dsalgo.algorithms.sorting.merge_sort import MergeSort

class MergeSortTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_merge_sort(self):
        A = [5,3,6,1,8,4]
        A_sort = [1,3,4,5,6,8]
        sorted_arr = MergeSort().sort(A=A)
        assert sorted_arr == A_sort
        
if __name__ == '__main__':
    unittest.main()