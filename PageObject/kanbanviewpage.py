from selenium.webdriver.common.by import By


class Kanbanview:

    def __init__(self, driver):
        self.driver = driver

    kanbanclick = (By.XPATH, "//a[@ptooltip='Kanban View']")
    Selecttaskdetail = (By.XPATH, "//div[@class='row']//div[2]//div[1]//div[3]//div[1]//div[2]//ul//li[1]//a//span")
    Statuselect = (By.XPATH, "//p[@class='autoClose']")
    Inprogress = (By.XPATH, "//div[@class='pri-option kanban-head']//div[2]")
    Priority1 = (By.XPATH, "//div[@class='resp-view']//div[1]//span")
    Lowpriority = (By.XPATH, "//p[@class='low-pr']")
    Assigncontactselect = (By.XPATH, "//div[@class='pri-align']//p//span//div[1]//div[1]//p-multiselect//div[1]//div[3]")
    contactselect = (By.XPATH, "//div[@class='ui-multiselect-items-wrapper']//ul//p-multiselectitem[2]//div[1]//div[1]")
    contactclose = (By.XPATH, '//a[@class="ui-multiselect-close ui-corner-all"]')
    dateclick = (By.XPATH, '//div[@class="group-kb-time d-none d-sm-block"]//div[1]//span')
    hourclear = (By.XPATH, '//div[@class="input-group epo-timer"]//epo-timer//div//form//div[1]//div[1]//input[@formcontrolname="hour"]')
    hourvalue = (By.XPATH, '//div[@class="input-group epo-timer"]//epo-timer//div//form//div[1]//div[1]//input[@formcontrolname="hour"]')
    minclear = (By.XPATH, '//div[@class="input-group epo-timer"]//epo-timer//div//form//div[1]//div[2]//input[@formcontrolname="min"]')
    minvalue = (By.XPATH, '//div[@class="input-group epo-timer"]//epo-timer//div//form//div[1]//div[2]//input[@formcontrolname="min"]')
    pmclick = (By.XPATH, '//div[@class="input-group epo-timer"]//epo-timer//div//form//div[1]//div[3]//label[@for="pm"]')
    eventadd = (By.XPATH, '//input[@id="mat-chip-list-input-3"]')
    Kanbanclose = (By.XPATH, '//div[@class="summary-cover"]//div[1]//app-task//div[@class="modal"][5]//div[1]//div[1]//div[1]//div[1]//i[@class="icon fa fa-times"]')

    def addbutton(self):
        return self.driver.find_element(*Kanbanview.kanbanclick)

    def selecttask(self):
        return self.driver.find_element(*Kanbanview.Selecttaskdetail)

    def statusselect(self):
        return self.driver.find_element(*Kanbanview.Statuselect)

    def inprogress(self):
        return self.driver.find_element(*Kanbanview.Inprogress)

    def priority(self):
        return self.driver.find_element(*Kanbanview.Priority1)

    def lowpriority(self):
        return self.driver.find_element(*Kanbanview.Lowpriority)

    def assigncontact(self):
        return self.driver.find_element(*Kanbanview.Assigncontactselect)

    def contactSelect(self):
        return self.driver.find_element(*Kanbanview.contactselect)

    def Contactclose(self):
        return self.driver.find_element(*Kanbanview.contactclose)

    def dateClick(self):
        return self.driver.find_element(*Kanbanview.dateclick)

    def Hourclear(self):
        return self.driver.find_element(*Kanbanview.hourclear)

    def Hourvalue(self):
        return self.driver.find_element(*Kanbanview.hourvalue)

    def Minclear(self):
        return self.driver.find_element(*Kanbanview.minclear)

    def Minvalue(self):
        return self.driver.find_element(*Kanbanview.minvalue)

    def Pmclick(self):
        return self.driver.find_element(*Kanbanview.pmclick)

    def Eventadd(self):
        return self.driver.find_element(*Kanbanview.eventadd)

    def kanbanclose(self):
        return self.driver.find_element(*Kanbanview.Kanbanclose)

