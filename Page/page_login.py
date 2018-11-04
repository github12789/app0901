import allure
from Base.base import Base
import Page
class PageLogin(Base):
    # 在page页面封装方法，不用刻意思考封装那几个方法，哪几部操作
    # 1.每部操作大度封装一个方法
    # 2.如果后期调用需要等多步操作封装成一个方法，那么就单独在封装一个方法
    # def page_input_username(self,username):
    #     self.base_input(login_username,username)
    # def page_input_password(self):
    # def page_click_login_btn(self):
    def page_click_me(self):
        self.base_click(Page.login_me)
    def page_click_name_ok_link(self):
        self.base_click(Page.login_name_ok_link)
    @allure.step("输入用户名:")
    def page_input_username(self,username):
        self.base_input(Page.login_username,username)
    @allure.step("输入密码:")
    def page_input_password(self,password):
        self.base_input(Page.login_password,password)
    @allure.step("点击登录:")
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)
    # 获取昵称，断言（公共方法）
    def page_get_nickname(self):
        return self.base_get_text(Page.login_nickname)
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(Page.login_setting)
    # 滑动也为公共方法，在Base内需要单独封装
    @allure.step("从消息推送-->滑到-->修改密码")
    def page_drag_and_drop(self):
        el1=self.base_find_element(Page.login_msg_send)
        el2=self.base_find_element(Page.login_modify_pwd)
        self.base_drag_and_drop(el1,el2)
    @allure.step("点击退出")
    def page_click_exit_btn(self):
        self.base_click(Page.login_logout)
    @allure.step("确认退出")
    def page_click_exit_btn_ok(self):
        self.base_click(Page.login_logout_ok)


