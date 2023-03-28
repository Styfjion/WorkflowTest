import unittest


class MyTestCase(unittest.TestCase):

    def test(self):
        test_list = [1, 1, 2]
        self.assertIsNotNone(test_list)


if __name__ == '__main__':
    unittest.main()
