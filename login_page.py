from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Base_tool import Base_tools
class Login(Base_tools):
    botton_page=(By.XPATH,'//*[@id="tab-outside"]')
    name = (By.XPATH, '//*[@placeholder="请输入用户名称"]')
    psw=(By.XPATH, '//*[@placeholder="请输入登录密码"]')
    login = (By.CSS_SELECTOR, '#pane-outside > form > div:nth-child(4) > div > button > span')
    usernames="wanghuimin"
    userpaw="Jinmaomj@2023"
    assert_login=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.navbar.main-page-he'
            'ader > div.navbar-top > div.navbar-right > div > button.el-button.el-button--primary.el-button--small > span')
    def Login_fram(self):
        self.click(self.botton_page)
    def username(self):
        self.send_keys(self.name,self.usernames)
    def userpassward(self):
        self.send_keys(self.psw,self.userpaw)
    def login_button(self):
        self.click(self.login)
    def login_assert(self):
         return self.Wait_element(self.assert_login).text

    # def login_assert(self):
    #     a = self.driver.find_element_by_css_selector(
    #         '#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.navbar.main-page-he'
    #         'ader > div.navbar-top > div.navbar-right > div > button.el-button.el-button--primary.el-button--small > span').text
    #     return a
    def login_case(self):
        self.max_windos()
        self.Login_fram()
        self.username()
        self.userpassward()
        self.login_button()
        #time.sleep(1)
        self.login_assert()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.get()
#     Login(driver)
