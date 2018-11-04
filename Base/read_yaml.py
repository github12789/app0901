import os
import yaml
class ReadYAML():
    def __init__(self,filename):
        self.file_path=os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yaml(self):
        # 打开文件返回读取数据
        with open(self.file_path,"r",encoding="utf-8") as f:
            # 读取文件内容
            return yaml.load(f)
    # 以下方法 作为右键运行调试所用
    def read_yaml01(self):
        with open("../Data/login_data.yaml","r",encoding="utf-8")as f:
            # yaml 的load方法进行读取
            return yaml.load(f)
if __name__ == '__main__':
    arrs=[]
    for data in ReadYAML("read_yaml.py").read_yaml01().values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    print(arrs)