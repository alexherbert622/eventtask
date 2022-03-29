from selenium.webdriver.common.by import By


class Calendarpage:

    def __init__(self, driver):
        self.driver = driver

    calendarclick = (By.XPATH, '//a[@ptooltip="Calender View"]')
    Dateclick = (By.XPATH, '//td[@data-date="2022-03-31"]//div[@class="fc-daygrid-day-events"]')
    Level3 = (By.XPATH, '//div[@class="parent col-md-12 col-lg-12 col-xl-12 col-sm-12"]//div[5]//p-dropdown//div[1]//div[3]')
    Levelselect = (By.XPATH, '//li[@aria-label="Medium"]')
    Status3 = (By.XPATH, '//div[@class="parent col-md-12 col-lg-12 col-xl-12 col-sm-12"]//div[6]//p-dropdown//div[1]//div[3]')
    Inprogress = (By.XPATH, '//li[@aria-label="In-Progress"]')
    Assign_contact = (By.XPATH, '//div[@class="parent col-md-12 col-lg-12 col-xl-12 col-sm-12"]//div[7]//p-multiselect//div[1]//div[3]')
    contactclick = (By.XPATH, '//div[@class="ui-multiselect-items-wrapper"]//ul//p-multiselectitem[2]//li//div[1]//div[1]')
    contactclose = (By.XPATH, '//a[@class="ui-multiselect-close ui-corner-all"]//span')
    calendarclose = (By.XPATH, '//div[@class="sidewrapper sidewrapper-type1 sidebaropen"]//div[1]//div[1]//button//i')

    def calendarclickbutton(self):
        return self.driver.find_element(*Calendarpage.calendarclick)

    def dateclick(self):
        return self.driver.find_element(*Calendarpage.Dateclick)

    def levelclick(self):
        return self.driver.find_element(*Calendarpage.Level3)

    def levelselect(self):
        return self.driver.find_element(*Calendarpage.Levelselect)

    def statusclick(self):
        return self.driver.find_element(*Calendarpage.Status3)

    def inprogress(self):
        return self.driver.find_element(*Calendarpage.Inprogress)

    def assigncontact(self):
        return self.driver.find_element(*Calendarpage.Assign_contact)

    def Contactclick(self):
        return self.driver.find_element(*Calendarpage.contactclick)

    def Contactclose(self):
        return self.driver.find_element(*Calendarpage.contactclose)

    def Calendarclose(self):
        return self.driver.find_element(*Calendarpage.calendarclose)