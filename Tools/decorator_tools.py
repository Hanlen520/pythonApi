# -*- coding: utf-8 -*-
"""
装饰器
"""
import time
from Tools.log import FrameLog
from Tools.date_helper import current_timestamp
from threading import Thread
import threading
from functools import wraps
from Config import config as cfg

save_mutex = threading.Lock()
log = FrameLog().log()


def retry_func(try_limit, log_show=True, send_dd=False, send_flag=""):
    """
    错误重试装饰器
    :param try_limit:
    :param log_show:
    :param send_dd:
    :param send_flag:
    :return:

     备注：若重试全部失败后，返回 31500
    """
    def try_func(func):
        def wrapper(*args, **kwargs):
            try_cnt = 0
            while try_cnt < try_limit:
                try:
                    st = time.time()
                    res = func(*args, **kwargs)
                    et = time.time()
                    if log_show:
                        log.info("%s: DONE %s" % (func.__name__, (et-st)))
                    return res
                except Exception as e:
                    time.sleep(1)
                    try_cnt += 1
                    if log_show:
                        log.error(e)
                        log.warning("%s: RETRY CNT %s" % (func.__name__, try_cnt))
            if log_show:
                log.warning("%s: FAILED" % func.__name__)
            if send_dd:
                if send_flag == "接口监控":
                    title = "[监控]'接口测试'"
                    text = "#### API自动化测试'接口无响应"
                    from Common.com_func import send_DD
                    send_DD(dd_group_id=cfg.DD_MONITOR_GROUP, title=title, text=text, at_phones=cfg.DD_AT_FXC, is_at_all=False)

            return 31500
        return wrapper
    return try_func


def async(func):
    """
    异步开线程调用
    :param func: 被修饰的函数
    :return:
    """
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


def elapse_time(func):
    """
    计算方法耗时
    :param func: 被修饰的函数
    :return:
    """
    def wrapper(*args, **kwargs):
        st = current_timestamp()
        res = func(*args, **kwargs)
        et = current_timestamp()
        log.info("%s ELAPSE TIME: %s" % (func.__name__, (et-st)/1000.0))
        return res
    return wrapper


def thread_save(func):
    @wraps(func)
    def processed_res(*args, **kwargs):
        save_mutex.acquire()
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        save_mutex.release()
        log.info(u"%s: DONE %s" % (func.__name__, (et-st)))
        return res
    return processed_res