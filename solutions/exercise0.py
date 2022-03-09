import unittest

"""
Small example written during ProgFest to showcase how to write a simple unit test in python. 
Initially from scratch, then using unittest library. 

1. Create a new script with a simple function like `mean(data)`. 
2. Proceed to write test functions from scratch to assert expected outcome. 
3. Import `unittest` and put these test functions inside a test class. 
"""


# 1. Create a new script with a simple function like `mean(data)`.

def mean(data):
    # This if-statement was added after writing 2nd test to bypass divisionByZeroError
    if len(data) == 0:
        return 0

    sum = 0
    for value in data:
        sum += value
    mean = sum / len(data)
    return mean


# 2. Write test functions from scratch to assert expected outcome.

def testMean():
    data = [0, 1, -1, 4]
    average = mean(data)
    assert average == 1
    print("Test passed !")


def testMeanWithNoData_shouldReturn0():
    noData = []
    average = mean(noData)
    assert average == 0
    print("Test passed !")


if __name__ == '__main__':
    testMean()
    testMeanWithNoData_shouldReturn0()


# 3. Import `unittest` and put these test functions inside a test class.
# At this point you should remove the code in step 2.

class TestMean(unittest.TestCase):
    def testMean(self):
        data = [0, 1, -1, 4]
        average = mean(data)
        self.assertEqual(1, average)
    
    def testMeanWithNoData_shouldReturn0(self):
        noData = []
        average = mean(noData)
        self.assertEqual(0, average)


if __name__ == '__main__':
    unittest.main()
