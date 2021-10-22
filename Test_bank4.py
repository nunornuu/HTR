from time import time

from bank import bank_addUser, bank_saveMoney, bank_takeMoney, bank_transformMoney
from ddt import ddt, data, unpack, file_data
import unittest


transformMoney = [
    # 0：正常，1：账号不存在，2：密码不对，3：钱不够'
    ['123456', '654321', '123456', 800, 0],
    ['65432', '123456', '123456', 800, 1],
    ['654321', '123486', '123456', 800, 1],
    ['123890', '123456', '123485', 800, 2],
    ['098765', '123890', '123456', 500, 3]
]


@ddt
class TestAddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @data(*transformMoney)
    @unpack
    def test_transformMoney(self, outputaccount, inputaccount, outputpassword, outputmoney, b):
        res = bank_transformMoney(outputaccount, inputaccount, outputpassword, outputmoney)
        self.assertEqual(res, b)


if __name__ == '__main__':
    unittest.main()







