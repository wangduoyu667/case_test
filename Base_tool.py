from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
class Base_tools:
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,loc):#loc传入元组
        return  self.driver.find_element(*loc)
    def Wait_element(self,loc):#返回元素
        return WebDriverWait(self.driver,3).until(Ec.visibility_of_element_located(loc))
    def send_keys(self,loc,value):
        self.Wait_element(loc).send_keys(value)
    def click(self,loc):
        self.Wait_element(loc).click()
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    def max_windos(self):
        self.driver.maximize_window()
if __name__ == '__main__':
    pass
