from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            'test_case_mixed_citations': ([3,0,6,1,5], 3),
            'test_case_low_citations': ([1,3,1], 1),
            'test_case_all_highly_cited': ([10,8,5,4,3], 4),
            'test_case_all_zero_citations': ([0,0,0,0], 0),
            'test_case_all_same_citations': ([5,5,5,5,5], 5),
            'test_case_increasing_citations': ([1,2,3,4,5,6], 3),
            'test_case_single_paper': ([100], 1),
            'test_case_two_papers_one_cited': ([0,10], 1),
            'test_case_minimum_input_size': ([0], 0),
            'test_case_minimum_input_non_zero': ([1], 1),
            'test_case_all_max_citations': ([1000]*5000, 5000),
            'test_case_all_zero_citations_max_length': ([0]*5000, 0),
            'test_case_half_cited_half_not': ([1000]*2500 + [0]*2500, 2500),
            'test_case_one_paper_with_all_citations': ([5000] + [0]*4999, 1),
            'test_case_descending_citations': (list(range(5000, 0, -1)), 5000)
        }
        self.__solution = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_mixed_citations(self):
        nums, output = self.__testcases['test_case_mixed_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_low_citations(self):
        nums, output = self.__testcases['test_case_low_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_all_highly_cited(self):
        nums, output = self.__testcases['test_case_all_highly_cited']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_all_zero_citations(self):
        nums, output = self.__testcases['test_case_all_zero_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))
    
    @timeout(0.5)
    def test_case_all_same_citations(self):
        nums, output = self.__testcases['test_case_all_same_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_increasing_citations(self):
        nums, output = self.__testcases['test_case_increasing_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_single_paper(self):
        nums, output = self.__testcases['test_case_single_paper']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_two_papers_one_cited(self):
        nums, output = self.__testcases['test_case_two_papers_one_cited']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_minimum_input_size(self):
        nums, output = self.__testcases['test_case_minimum_input_size']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_minimum_input_non_zero(self):
        nums, output = self.__testcases['test_case_minimum_input_non_zero']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_all_max_citations(self):
        nums, output = self.__testcases['test_case_all_max_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_all_zero_citations_max_length(self):
        nums, output = self.__testcases['test_case_all_zero_citations_max_length']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_half_cited_half_not(self):
        nums, output = self.__testcases['test_case_half_cited_half_not']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_one_paper_with_all_citations(self):
        nums, output = self.__testcases['test_case_one_paper_with_all_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

    @timeout(0.5)
    def test_case_descending_citations(self):
        nums, output = self.__testcases['test_case_descending_citations']
        self.assertEqual(output, self.__solution.hIndex(nums))

if __name__ == '__main__': unittest.main()