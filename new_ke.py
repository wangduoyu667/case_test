from selenium.webdriver.common.by import By
from Base_tool import Base_tools
class Kh_new(Base_tools):
    # url='http://10.160.152.88/login'
    # botton_page=(By.XPATH,'//*[@id="tab-outside"]')
    # name = (By.XPATH, '//*[@placeholder="请输入用户名称"]')
    # psw=(By.XPATH, '//*[@placeholder="请输入登录密码"]')
    # login = (By.CSS_SELECTOR, '#pane-outside > form > div:nth-child(4) > div > button > span')
    # usernames="wanghuimin"
    # userpaw="Jinmaomj@2023"
    # def Login_fram(self):
    #     self.click(self.botton_page)
    # def username(self):
    #     self.send_keys(self.name,self.usernames)
    # def userpassward(self):
    #     self.send_keys(self.psw,self.userpaw)
    # def login_button(self):
    #     self.click(self.login)
    home_button=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[2]/div/ul/div[2]/li/div/span')
    button_kh=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[2]/div/ul/div[2]/li/ul/div[3]/li/span')
    new_kh_button=(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div/button/'
                            'span')
    #新建客户界面
    new_wid_button=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.fl'
                                    'ex-row.flex1 > div > div > div:nth-child(4) > div > div > div > section > div > '
                                    'div.dictionary-detail-condition > form > div:nth-child(1) > div:nth-child(1) > div '
                                    '> div > div > span > span > i')
    select_gerenkehu=(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdo'
                                      'wn__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span')
    select_qiyekehu = (By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scro'
                     'llbar__wrap > ul > li.el-select-dropdown__item.hover > span')

    # def login_case(self):
    #     self.Login_fram()
    #     self.username()
    #     self.userpassward()
    #     self.login_button()
    def button_home(self):
        self.click(self.home_button)
    def click_ck(self):
        self.click(self.button_kh)
    def click_new_kh_button(self):
        self.click(self.new_kh_button)
    def click_new_wid_button(self):
        self.click(self.new_wid_button)
    def new_creat_gerenhehu(self):
        self.button_home()
        self.click_ck()
        self.click_new_kh_button()
        self.click_new_wid_button()
    def new_creat_qiyekehu(self):
        self.button_home()
        self.click_ck()
        self.click_new_kh_button()
        self.click_new_wid_button()

