import logging
import time
import os.path

class Logger:
    def __init__(self,logger):
        self.logger=logging.getLogger(logger) #实例化logger对象
        self.logger.setLevel(logging.DEBUG) #设置级别

        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+'/logs/'
        log_name=log_path+rq+'.log'

        fh=logging.FileHandler(log_name) #文件
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()  # 控制台
        ch.setLevel(logging.INFO)

        format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(format)
        ch.setFormatter(format)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
    def getlog(self):
        return self.logger




