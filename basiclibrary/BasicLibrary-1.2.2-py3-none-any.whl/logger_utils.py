import time
from nb_log import LogManager

'''
日志按日生成
'''
now_time = time.strftime('%Y_%m_%d')
logger = LogManager().get_logger_and_add_handlers(log_filename=now_time+'ApiTest.log')