from time import time

from bank import bank_addUser, bank_saveMoney, bank_takeMoney, bank_transformMoney
from ddt import ddt, data, unpack, file_data
import unittest


addUser = [
    # 1：成功，2：用户已存在，3：用户库已满
    ['no1', '123456', 'cn', 'cn', 'cn', '23', 2000, 2],
    ['no5', '123456', 'cn', 'cn', 'cn', '23', 3000, 1],
    ['no5', '123456', 'cn', 'cn', 'cn', '03', 5000, 2],
]


@ddt
class TestAddUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @data(*addUser)
    @unpack
    def test_addUser(self, username, password, country, province, street, door, money, t):
        res = bank_addUser(username, password, country, province, street, door, money)

        self.assertEqual(res, t)


if __name__ == '__main__':
    unittest.main()








