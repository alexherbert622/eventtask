from selenium.webdriver.common.by import By


class Listingpage:

    def __init__(self, driver):
        self.driver = driver

    Listingclick = (By.XPATH, '//a[@ptooltip="List View"]')
    Edittask = (By.XPATH, '//table//tbody//tr[1]//td//span[@ptooltip="Edit"]')
    Level2 = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[5]//p-dropdown//div[1]//div[3]")
    Inprogress = (By.XPATH, '//li[@aria-label="Medium"]')
    status2 = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[6]//p-dropdown//div[1]//div[3]")
    statuslevel = (By.XPATH, '//li[@aria-label="In-Progress"]')
    Assign_Contact1 = (By.XPATH, "//div[@class='parent col-md-12 col-lg-12 col-xl-12 col-sm-12']//div[7]//p-multiselect//div[1]//div[3]")
    contactclick = (By.XPATH, "//div[@class='ui-multiselect-items-wrapper']//ul//p-multiselectitem[2]//li//div[1]//div[1]")
    contactclose = (By.XPATH, "//a[@class='ui-multiselect-close ui-corner-all']//span")
    tagclick = (By.XPATH, "//div[@class='sidewrapper sidewrapper-type1 sidebaropen']//div[1]//div[2]//div[2]//div[1]//div[8]//mat-chip-list//div[1]//input")
    listingclose = (By.XPATH, '//div[@class="sidewrapper sidewrapper-type1 sidebaropen"]//div[1]//div[1]//button//i')


    def listingbutton(self):
        return self.driver.find_element(*Listingpage.Listingclick)

    def edittask(self):
        return self.driver.find_element(*Listingpage.Edittask)

    def prioritylevel(self):
        return self.driver.find_element(*Listingpage.Level2)

    def inprogress(self):
        return self.driver.find_element(*Listingpage.Inprogress)

    def Statusclick(self):
        return self.driver.find_element(*Listingpage.status2)

    def Statuslevel(self):
        return self.driver.find_element(*Listingpage.statuslevel)

    def Assigncontact(self):
        return self.driver.find_element(*Listingpage.Assign_Contact1)

    def Contacclick(self):
        return self.driver.find_element(*Listingpage.contactclick)

    def Contactclose(self):
        return self.driver.find_element(*Listingpage.contactclose)

    def Addtag(self):
        return self.driver.find_element(*Listingpage.tagclick)

    def Listingclose(self):
        return self.driver.find_element(*Listingpage.listingclose)