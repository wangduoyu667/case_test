from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://10.160.152.88")
driver.find_element_by_id("tab-outside").click()
driver.find_element_by_xpath('//*[@placeholder="请输入用户名称"]').send_keys("wanghuimin")
driver.find_element_by_xpath('//*[@placeholder="请输入登录密码"]').send_keys("Jinmaomj@2023")
driver.find_element_by_css_selector('#pane-outside > form > div:nth-child(4) > div > button > span').click()
time.sleep(1)
a=driver.find_element_by_css_selector('#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.navbar.main-page-he'
                                    'ader > div.navbar-top > div.navbar-right > div > button.el-button.el-button--primary.el-button--small > span').text
print(a)
driver.find_element_by_xpath("//*[text()='商机线索']").click()