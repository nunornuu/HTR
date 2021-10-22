import unittest
from calc import Calc
from ddt import ddt, data, unpack


add_data = [[1, 2, 3], [0, 3, 3], [0, -5, -5], [-1, 8, 7]]
sub_data = [[1, 2, -1], [5, 3, 2], [0, -5, 5], [0, 8, -8], [2, 0, 2]]


@ddt
class CalcTest(unittest.TestCase):

    @data(*add_data)
    @unpack
    def test_add(self, a, b, c):
        calc1 = Calc()
        re = calc1.add(a, b)
        self.assertEqual(c, re)

    @data(*sub_data)
    @unpack
    def test_sub(self, a, b, c):
        calc1 = Calc()
        re = calc1.sub(a, b)
        self.assertEqual(c, re)


if __name__ == '__main__':
    unittest.main()
