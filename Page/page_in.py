# 统一page页面对象管理，主要解决对page页的统一管理，解决批量导入page问题，解决driver的问题
# 利用类与方法的机制，在统一管理入口类，新建获取多个页面对象方法
from Base.get_driver import get_driver
from Page.page_login import PageLogin
class PageIn():
    def __init__(self):
        self.driver=get_driver()
        # Base.__init__(self,driver) # Base类的初始化方法 也可以用这种方法
    # 获取page_login页面对象
    def page_get_login(self):
        # 实例化pagelogin封装类
        return PageLogin(self.driver)

