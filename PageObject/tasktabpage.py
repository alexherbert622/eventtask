from selenium.webdriver.common.by import By


class tasktabpage:

    def __init__(self, driver):
        self.driver = driver

    Tasktab = (By.ID, "task-tab")

    def Taskpage(self):
        return self.driver.find_element(*tasktabpage.Tasktab)