import pytest
from Pages.BasePage import BasePage
from Pages.RegistrationPage import Registration
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log=Logger(__name__,logging.INFO)


class TestSignUpTest(BaseTest):

    @pytest.mark.parametrize("name,phonenumber,email,country,city,username,password", dataProvider.get_data("LoginTest"))
    def test_doSignUp(self,name,phonenumber,email,country,city,username,password):
         # self.driver = get_browser
         log.logger.info("Test Do Signup started")
         regPage=Registration(self.driver)
         regPage.fillForm(name,phonenumber,email,country,city,username,password)
         log.logger.info("Test Do Signup successfully executed")



