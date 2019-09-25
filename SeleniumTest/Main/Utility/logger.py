import inspect
import logging
import os


def function_logger(file_level, console_level = None):
    function_name = inspect.stack()[1][3]  # get calling function name
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)  # By default, logs all messages
    logfile=os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/TestLogs/{0}.log".format(function_name)

    if console_level != None:
        ch = logging.StreamHandler()  # StreamHandler logs to console
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    # delete .log file if exist
    if os.path.isfile(logfile):
        os.remove(logfile)

    fh = logging.FileHandler(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/TestLogs/{0}.log".format(function_name))
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger
