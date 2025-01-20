from Pages.BasePage import BasePage

class NewCarsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def selectHyundau(self):
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        print("inside select bmw")
        self.click("bmw_XPATH")

    def selectHonda(self):
        self.click("kia_XPATH")