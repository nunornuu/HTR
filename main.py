from time import time

from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread


# unittest默认测试加载器


def action(n, path=os.getcwd(), name='',):
    test = unittest.defaultTestLoader.discover(path,name)
    runner = HTMLTestRunner.HTMLTestRunner(
        title='测试报告',
        description='测试报告',
        verbosity=1,
        stream=open(f'filename{n}.html', 'w', encoding='utf-8')
    )
    runner.run(test)


test1 = Thread(target=action, args=(1, os.getcwd(), 'Test_bank1.py'))
test2 = Thread(target=action, args=(2, os.getcwd(), 'Test_bank2.py'))
test3 = Thread(target=action, args=(3, os.getcwd(), 'Test_bank3.py'))
test4 = Thread(target=action, args=(4, os.getcwd(), 'Test_bank4.py'))

start = time()
test1.start()
test1.join()
test2.start()
test2.join()
test3.start()
test3.join()
test4.start()
test4.join()
end = time()

print(f'共用时长：{end - start}')
# runner = HTMLTestRunner.HTMLTestRunner(
#     title='测试报告',
#     description='测试报告',
#     verbosity=1,
#     stream=open(f'filename{n}.html', 'w', encoding='utf-8')
# )

# run函数运行给定的测试用例或测试套件。
# runner.run(test1)
# runner.run(test2)
# runner.run(test3)
# runner.run(test4)

