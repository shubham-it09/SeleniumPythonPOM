from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("fineNewCAR_XPATH")
        return NewCarsPage(self.driver)


    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass