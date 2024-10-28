import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3
    def test1_time_add(self):
        input1 = data.Time(1,1,40)
        input2 = data.Time(1,5,50)
        result = lab5.time_add(input1, input2)
        expected = data.Time(2,7,30)
        self.assertEqual(expected, result)
    def test2_time_add(self):
        input1 = data.Time(0,0,40)
        input2 = data.Time(0,0,20)
        result = lab5.time_add(input1, input2)
        expected = data.Time(0,1,00)
        self.assertEqual(expected, result)

    # Part 4
    def test1_is_descending(self):
        input1 = [5,4,3,2,1]
        result = lab5.is_descending(input1)
        expected = True
        self.assertEqual(expected, result)
    def test2_is_descending(self):
        input1 = [5,4,6,2,1]
        result = lab5.is_descending(input1)
        expected = False
        self.assertEqual(expected, result)

    # Part 5
    def test1_largest_between(self):
        input1 = [6,2,5,4,3]
        result = lab5.largest_between(input1,1,4)
        expected = 2
        self.assertEqual(expected, result)
    def test2_largest_between(self):
        input1 = [6,2,5,4,3]
        result = lab5.largest_between(input1,4,1)
        expected = None
        self.assertEqual(expected, result)

    # Part 6





if __name__ == '__main__':
    unittest.main()
