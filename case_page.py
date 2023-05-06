from selenium import webdriver
import unittest
import time
from Base_tool import Base_tools
from login_page import Login
from new_hezuoshang import New_hezuoshang
from new_ke import Kh_new
class Mj_case(unittest.TestCase,Login,Kh_new,New_hezuoshang):
    @classmethod
    def setUpClass(self) -> None:
        url='http://10.160.152.88/login'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        c=Base_tools(self.driver)#传递参数给基类，用于调用方法
    @classmethod
    def tearDownClass(self) -> None:
        time.sleep(2)
        #self.driver.quit()
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_case01(self):
        self.login_case()
        self.assertEqual(self.login_assert(),"安全退出",msg='断言失败')
    def test_case02(self):
        #self.login_case()
        #time.sleep(2)
        self.create_new()

if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(Mj_case('test_case01'))
    suit.addTest(Mj_case('test_case02'))
    runner=unittest.TextTestRunner()
    runner.run(suit)
    #unittest.main(verbosity=1)
