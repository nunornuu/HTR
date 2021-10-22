from time import time

from bank import bank_addUser, bank_saveMoney, bank_takeMoney, bank_transformMoney
from ddt import ddt, data, unpack, file_data
import unittest


saveMoney = [
    # True 成功 ,False 失败
    ['123456', 900, True],
    ['654322', 900, False],

]


@ddt
class TestAddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @data(*saveMoney)
    @unpack
    def test_saveMoney(self, ac, money, c):
        res = bank_saveMoney(ac, money)
        self.assertEqual(res, c)


if __name__ == '__main__':
    unittest.main()







