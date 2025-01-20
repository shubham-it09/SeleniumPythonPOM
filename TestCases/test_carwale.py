import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger


log=Logger(__name__,logging.INFO)


class TestCarwale(BaseTest):
    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("********inside new car test**************")
        home= HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(5)

    @pytest.mark.parametrize("carBrand,carTitle",dataProvider.get_data("NewCarTest"))
    def test_selectCars(self, carBrand,carTitle):
        log.logger.info("********inside new car test**************")
        home= HomePage(self.driver)
        car=CarBase(self.driver)

        if carBrand=="BMW":
            print("inside bmw")
            home.gotoNewCars().selectBMW()
            time.sleep(5)
            title=car.carTitle()
            print(title)
            assert title == carTitle, "not on the correct page"
            car.getCarNameAndPrices()
        elif carBrand=="Toyota":
            home.gotoNewCars().selectToyota()
            time.sleep(5)
            title = car.carTitle()
            print(title)
            assert title == carTitle, "not on the correct page"
            car.getCarNameAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            time.sleep(5)
            title = car.carTitle()
            assert title == carTitle,"not on the correct page"
            car.getCarNameAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundau()
            time.sleep(5)
            title = car.carTitle()
            assert title==carTitle, "not on the correct page"
            print("car title is " + title)
            car.getCarNameAndPrices()



