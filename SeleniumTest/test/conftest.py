import pytest
from Main.Generic.BaseTest import *
from Main.Utility.htmllogger import HTMlLogger
from Main.Utility.ExcelReader import ReadLine


@pytest.fixture()               # scope="class" -> default scope is function
def setup(request):
    logger = HTMlLogger()       # function_logger(logging.INFO, logging.ERROR)
    baseTest().TestCaseInit(logger)
    request.cls.logger = logger
    request.cls.currentRow = ReadLine("TestData.xlsx",request.function.__name__)   # pass Test case id as call fun name
    yield
    baseTest().TestCaseExit(logger)
