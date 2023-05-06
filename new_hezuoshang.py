from selenium.webdriver.common.by import By
from Base_tool import Base_tools
class New_hezuoshang(Base_tools):
    home_button=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[2]/div/ul/div[5]/li/div/i[2]')#主页合作商按钮
    list_button1=(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[2]/div/ul/div[5]/li/ul/div[1]/li/span')#合作商列表按钮
    list_button2 = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button/span')  # 添加合作商按钮
    #新建合作商界面
    hezuosleixing=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-ad'
                                   'd-tab.g-search-box > form > div:nth-child(1) > div:nth-child(1) > div > div > div > div > span > span > i')#合作商类型下拉
    select_qiyekehu=(By.CSS_SELECTOR,'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdo'
                                      'wn__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span')#选择企业客户
    select_gerenkehu = (By.CSS_SELECTOR, 'body > div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dro'
                                        'pdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover > span')#选择个人客户
    select_hezuoshangmingchen=(By.XPATH,'//*[@placeholder="请输入合作商名称"]')#合作商名称

    button_nashuirenlist=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-con'
                                          'tent.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(1) > div:nth-child(3) > div > div > div > div > span > span > i')#纳税人列表下拉
    select_yibannashuiren = (By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap >'
                     ' ul > li:nth-child(1) > span')  # 选择一般纳税人
    select_xiaoguimonashuiren = (By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > u'
                     'l > li.el-select-dropdown__item.hover > span')  # 选择小规模纳税人

    button_zhengjian_type=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-co'
                                           'ntent.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(2) > div:nth-child(1) > div > div > div > div > span > span > i')#证件类型列表下拉
    select_yingyezhizhao = (By.CSS_SELECTOR, 'body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wrap.'
                                             'el-scrollbar__wrap > ul > li:nth-child(1) > span')  # 选择营业执照
    select_zuzhijigoudaima = (By.CSS_SELECTOR, 'body > div:nth-child(8) > div.el-scrollbar > div.el-select-dropdown__wra'
                                               'p.el-scrollbar__wrap > ul > li.el-select-dropdown__item.selected.hover > span')  # 选择组织机构代码

    select_zhengjianhaoma = (By.XPATH, '//*[@placeholder="请输入证件号码"]')  # 证件号码
    button_tongyibianma=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-con'
                                         'tent.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(2) > div:nth-child(3) > div > div > button > span')#统一编码按钮
    select_hezuoshanglianxiren = (By.XPATH, 'placeholder="请输入合作商联系人"')  # 合作商联系人
    select_hezuoshangdianhua = (By.XPATH, 'placeholder="请输入合作商电话"')  # 合作商电话

    button_zhongxinchengshi=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page'
                                             '-content.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(3) > div:nth-child(3) > div > div > div > div > span > span > i')#归属中心城市下拉列表
    select_zhongxinchengshi_shanghai = (By.CSS_SELECTOR, "//*[text()='上海-中心城市公司']")  # 中心城市上海

    button_hezuoshang_sharp_ruzhu=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main'
                                                   '-page-content.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(4) > div:nth-child(1) > div > div > label:nth-child(1) > span.el-checkbox__input > span')#合作商标签入驻
    button_hezuoshang_sharp_ziying = (By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-'
                                                      'content.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(4) > div:nth-child(1) > div > div > label:nth-child(2) > span.el-checkbox__input > span')  # 合作商标签自营

    button_yewufanwei=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.flex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(4) > div:nth-chil'
                                       'd(2) > div > div > div > div.el-input.el-input--medium.el-input--suffix.is-focus > span > span > i(3) > div:nth-child(3) > div > div > div > div > span > span > i')#业务范围下拉列表
    select_yewufanwei_quanwudingzhi = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]")  # 全屋定制[1]

    select_zhucedizhi=(By.XPATH,'//*[@placeholder="请输入注册地址"]')
    #附件上传
    button_fujian=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.fl'
                                   'ex-row.flex1 > div > div > div > div.flex1.flex-col.project-add-tab.g-search-box > form > div:nth-child(5) > div > div > div > div > div > div')#附件上传按钮
    button_fujian_type=(By.XPATH,'/html/body/div[5]/div/div[2]/div/for'
                                 'm/div/div[1]/div/div/div/div/span/span/i')#附件上传类型列表
    select_fujian_yingyezhizhao=(By.XPATH,'/html/body/div[7]/div[1]/div[1]/ul/li[1]')#营业执照
    select_fujian_kaihuxuke = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]')  # 银行开户许可证
    select_fujian_shenfenzheng = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]')  # 法人身份证复印件
    select_fujian_caiwubaobiao = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]')  # 财务报表
    select_fujian_qiyeqixin = (By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul/li[1]')  # 企业资信
    button_xuanzhefujian=(By.XPATH,'/html/body/div[5]/div/div[2]/div/'
                                   'form/div/div[2]/div/div/div/div/button/span')#选择附件上传
    button_shangchuan = (By.XPATH, '/html/body/div[5]/di'
                                   'v/div[2]/div/form/div/div[3]/div/div/div/button[2]/span')  # 上传按钮
    button_queding=(By.CSS_SELECTOR,'body > div.el-dialog__wrapper > div > div.el-dialog__footer > span > button.el-butt'
                                    'on.el-button--primary.el-button--small > span')#确定按钮
    button_save=(By.CSS_SELECTOR,'#app > div > div > div.main-page-body.flex-col.flex1.of-h > div.main-page-content.fle'
                                 'x-row.flex1 > div > div > div > div:nth-child(2) > button.el-button.save-button.el-button--primary.el-button--small > span')#保存按钮

    def create_new(self):#进入创建合作商界面
        self.switch_window()
        self.click(self.home_button)
        # self.click(self.list_button1)
        # self.click(self.list_button2)
    # def hezuoshang_type_geren(self):#合作商类型选择个人
    #     self.click(self.hezuosleixing)
    #     self.click(self.select_gerenkehu)
    # def hezuoshang_type_qiye(self):#合作商类型选择企业
    #     self.create_new()#创建合作商


