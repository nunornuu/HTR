from time import time

from bank import bank_addUser, bank_saveMoney, bank_takeMoney, bank_transformMoney
from ddt import ddt, data, unpack, file_data
import unittest


takeMoney = [
    # 0：正常，1：账号不存在，2：密码不对，3：钱不够'
    ['123456', '123456', 200, 0],
    ['123899', '123456', 200, 1],
    ['654321', '1234566', 200, 2],
    ['098765', '123456', 2000, 3]
]


@ddt
class TestAddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @data(*takeMoney)
    @unpack
    def test_takeMoney(self, account, password, money, b):
        res = bank_takeMoney(account, password, money)
        self.assertEqual(res, b)


if __name__ == '__main__':
    unittest.main()







