import Code_Coverage.math as math
import unittest


class AddTest(unittest.TestCase):
    def Test_add(self):
        result = math.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()

