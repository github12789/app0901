import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base():
    # 谁实例化我，我先执行谁
    def __init__(self,driver):
        self.driver=driver

    #  查找元素单独封装，给下面方法使用
    # 1.封装查找元素的时候记得使用显示等待
    # 2.最后要通过return进行返回元素
    def base_find_element(self,loc,timeout=30,poll=0.5): #ctrl+p 可以看需要填的元素
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素封装
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 元素输入封装
    def base_input(self,loc,text):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(text)

    # 截图封装
    def base_get_screenshot(self):
        # 调用的时候使用的是pytest，一定要使用路径os.getcwd()
        img_path=os.getcwd()+os.sep+"Image"+os.sep+"faild.png"  # 动态获取
        # 由于失败截图后，我们动态写入指定路径的报告里面
        self.driver.get_screenshot_as_file(img_path)

    # 获取toast封装，提示框
    def base_get_toast(self,message):
        # 拼接字符串
        msg = By.XPATH,"//*[contains(@text,'"+message+"')]"
        # 调用查找元素方法 获取文本方法并返回
        el = self.base_find_element(msg, poll=0.1)
        return el.text
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2) #el1起点元素，落点元素
