from selenium.webdriver.common.by import By


class Addnewevent:

    def __init__(self, driver):
        self.driver = driver

    clicknewevent = (By.XPATH, '//i[@class="fa fa-plus add-temp"]')
    Eventname = (By.ID, 'itemname')
    Eventdescription = (By.XPATH, '//input[@placeholder="Task Description"]')
    datebuttonclick = (By.XPATH, '//div[@class="form-group task-date-custom"]//mat-form-field//div[1]//div[1]//div[2]//mat-datepicker-toggle//button')
    dateselect = (By.XPATH, '//td[@aria-label="March 15, 2022"]')
    timebuttonclick = (By.XPATH, '//div[@class="input-group  epo-timer"]//span')
    timehourclear = (By.XPATH, '//input[@formcontrolname="hour"]')
    timehourinsert = (By.XPATH, '//input[@formcontrolname="hour"]')
    timeminclear = (By.XPATH, "//input[@formcontrolname='min']")
    timemininsert = (By.XPATH, "//input[@formcontrolname='min']")
    timepmclick = (By.XPATH, '//label[@for="pm"]')
    selectstatus = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[6]//p-dropdown//div[1]//div[3]")
    Inprogress = (By.XPATH, '//li[@aria-label="In-Progress"]')
    priorityselect = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[5]//p-dropdown//div[1]//div[3]")
    Mediumselect = (By.XPATH, '//li[@aria-label="Medium"]')
    Assign_Contact = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[7]//p-multiselect//div[1]//div[3]")
    Assigncontactclick = (By.XPATH, '//div[@class="ui-multiselect-items-wrapper"]//ul//p-multiselectitem[2]//div[1]//div[1]')

    def addnewbutton(self):
        return self.driver.find_element(*Addnewevent.clicknewevent)

    def eventname(self):
        return self.driver.find_element(*Addnewevent.Eventname)

    def eventdesc(self):
        return self.driver.find_element(*Addnewevent.Eventdescription)

    def Datebuttonclick(self):
        return self.driver.find_element(*Addnewevent.datebuttonclick)

    def Dateselect(self):
        return self.driver.find_element(*Addnewevent.dateselect)

    def Timeclick(self):
        return self.driver.find_element(*Addnewevent.timebuttonclick)

    def Timehourclear(self):
        return self.driver.find_element(*Addnewevent.timehourclear)

    def Timehourinsert(self):
        return self.driver.find_element(*Addnewevent.timehourinsert)

    def Timeminclear(self):
        return self.driver.find_element(*Addnewevent.timeminclear)

    def Timemininsert(self):
        return self.driver.find_element(*Addnewevent.timemininsert)

    def Timepmclick(self):
        return self.driver.find_element(*Addnewevent.timepmclick)

    def Selectstatus(self):
        return self.driver.find_element(*Addnewevent.selectstatus)

    def inprogress(self):
        return self.driver.find_element(*Addnewevent.Inprogress)

    def Priorityselect(self):
        return self.driver.find_element(*Addnewevent.priorityselect)

    def mediumselect(self):
        return self.driver.find_element(*Addnewevent.Mediumselect)

    def assign_contact(self):
        return self.driver.find_element(*Addnewevent.Assign_Contact)

    def assigncontactclick(self):
        return self.driver.find_element(*Addnewevent.Assigncontactclick)