from appium import webdriver
def get_driver():
            # 服务端启动参数
    desired_caps = {}
            # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
            # 设备号
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 指定appium框架版本 获取toast消息必须 指定以下参数
    desired_caps['automationName'] = 'Uiautomator2'
    # 包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
            # 启动名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
            # 手机驱动对象
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver # 返回driver对象
