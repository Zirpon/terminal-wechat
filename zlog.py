import logging

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')

# DEBUG < INFO < WARNING < ERROR < CRITICAL
#用字典保存日志级别
format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
}

mapGroupLogger = {}
mapFriendLogger = {}

def getLogger(logType, logname):
    if logType == "Group" :
        mapGroupLogger[logname] = mapGroupLogger.get(logname) or Logger(logname="./log/GroupChat.log", loglevel=1, logger=logname).getlog()
        return  mapGroupLogger[logname]
    elif logType == "Friend" :
        mapFriendLogger[logname] = mapFriendLogger.get(logname) or Logger(logname="./log/FriendChat.log", loglevel=1, logger=logname).getlog()
        return  mapFriendLogger[logname]
    else:
        return None


class Logger():
    def __init__(self, logname, loglevel, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename=logname, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s [%(name)s][%(levelname)s]:%(message)s')
        #formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
    
    def getlog(self):
        return self.logger