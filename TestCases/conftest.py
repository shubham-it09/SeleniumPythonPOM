import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from Pages import NewCarsPage
from Utilities import configReader





# driver = None
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )
#
# @pytest.fixture(scope="class")
# def get_browser(request):
#     global driver
#     browser_name=request.config.getoption("browser_name")
#
#     if browser_name=="chrome":
#
#         driver = webdriver.Chrome()
#
#     elif browser_name=="firefox":
#         print("this is firefox")
#     elif browser_name == "edege":
#         print("this is edege")
#     # driver.get(configReader.readConfig("basic info", "testsiteurl"))
#     driver.get("qa.way2automation.com")
#
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)



@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    if request.param == "chrome":
        driver=webdriver.Chrome()
    # if request.param == "firefox":
    #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    print("url is "+configReader.readConfig("basic info", "testsiteurl"))
    # driver.get(str(configReader.readConfig("basic info", "testsiteurl")))
    request.cls.driver=driver
    # driver.get("https://way2automation.com/way2auto_jquery/index.php")
    driver.get("https://www.carwale.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()