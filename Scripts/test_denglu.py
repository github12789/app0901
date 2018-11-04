# 导路径
import sys,os
sys.path.append(os.getcwd())
from Base.read_yaml import ReadYAML
from Page.page_in import PageIn
import pytest
import allure
# 读取参数函数 封装
def get_data():
    arrs = []
    # 获取出的结果为列表，列表内单个元素值为字典data_values()
    for data in ReadYAML("login_data.yaml").read_yaml().values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    return arrs
class TestLogin():
    # setup
    @allure.step("开始执行初始化函数")
    def setup_class(self):
        # 实例化统一入口类
        allure.attach("步骤描述","实例化统一入口类")
        self.page = PageIn()
        allure.attach("步骤描述","实例化login页面对象")
        self.login=self.page.page_get_login()
        """
        说明，使用统一入口类，调用页面对象的方法是匿名调用的好？还是实名实例化的好
        1.如果此类只用一次，一定推荐匿名
        2.如果此类使用多次，推荐使用实名 
        """
        allure.attach("步骤描述：","点击我")
        self.login.page_click_me()
        allure.attach("步骤描述：","点击已有账号去登录")
        self.login.page_click_name_ok_link()
    # teardown
    def teardown_class(self):
        allure.attach("步骤描述：","关闭驱动对象")
        self.login.driver.quit()
    # 测试方法
    @allure.step("开始执行测试脚本")
    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    def test_login(self,username,password,expect_result,expect_toast):
        if expect_result:
            try:
            # 输入用户名
                self.login.page_input_username(username)
            # 输入密码
                self.login.page_input_password(password)
            # 点击登录
                self.login.page_click_login_btn()
            # 获取昵称，断言
                nickname = self.login.page_get_nickname()
                allure.attach("开始判断是否登录成功", " ")
                assert expect_result in nickname
                allure.attach("登录成功！", " ")
                # 设置
                self.login.page_click_setting()
                # 滑动
                self.login.page_drag_and_drop()
                # 点击退出
                self.login.page_click_exit_btn()
                # 确认退出，注意：要关注退出后的停留界面，因为循环遍历用例
                self.login.page_click_exit_btn_ok()
                # 点击我
                self.login.page_click_me()
                # 点击 已有账号去登录
                self.login.page_click_name_ok_link()
            except:
                # 截图
                self.login.base_get_screenshot()
                # 写入报告
                with open("./Image/faild.png","rb") as f:
                # 写入图片、视频用rb,写入二进制；另外和scripts同级是./，下级是../
                # 使用attch参数，第一个为描述，第二个图片流，第三个图片格式
                    allure.attach("失败原因请看附件图", f.read(), allure.attach_type.PNG)
                # 抛异常
                raise
        else:
            try:
                # 输入用户名
                self.login.page_input_username(username)
                # 输入密码
                self.login.page_input_password(password)
                # 点击登录
                self.login.page_click_login_btn()
                # 断言
                """
                    说明：
                        1. 调用获取toast消息封装方法，传入全部匹配值：也就是预期结果，获取元素的文本
                        2. 让获取结果和预期结果做对比;
                    注意：这里的 expect_toast和传入的匹配参数是相同的，不要混淆
                """
                assert expect_toast in self.login.base_get_toast(expect_toast)
            except:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open("./Image/faild.png","rb") as f:
                    allure.attach("失败原因请查看附加图：",f.read(),allure.attach_type.PNG)






















