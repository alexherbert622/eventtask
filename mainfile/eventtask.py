####################
# Name:event task module
# Description: To do some operation
# Author: Alex herbert
# Date: 16-03-2022
####################
# Library used #
import time
import sys
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Homepage import Homepage
from PageObject.addnewevent import Addnewevent
from PageObject.calendarpage import Calendarpage
from PageObject.eventdiarypage import eventdiarypage
from PageObject.kanbanviewpage import Kanbanview
from PageObject.listingpage import Listingpage
from PageObject.login_page import Loginpage
from PageObject.tasktabpage import tasktabpage
from Testdata.datareadwritefile import Datareadfile, datawritepass, datawritefail
from Utilities.BaseClass import Baseclass


@allure.severity(allure.severity_level.NORMAL)
class TestEpo(Baseclass):

    def test_unamepwd(self):
            datareadusername = Datareadfile.username
            datareadpwd = Datareadfile.password
            loginpage = Loginpage(self.driver)
            wait = WebDriverWait(self.driver, 6)
            wait.until(EC.presence_of_element_located((By.NAME, "userNameOrEmail")))
            loginpage.usernameoremail().send_keys(datareadusername)
            loginpage.password().send_keys(datareadpwd)

    try:
        def test_login_button(self):
            homepage = Homepage(self.driver)
            loginpage = Loginpage(self.driver)
            loginpage.loginbutton().click()
            time.sleep(5)
            homepage.popup().click()
    except Exception as e:
        linenum = sys.exc_info()[2].tb_lineno
        print("error on line number:"+str(linenum)+str(e))
        def test_failedcase(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testfailedscreen",
                        attachment_type=AttachmentType.PNG)
            msg2 = datawritefail()
            self.driver.close()
    finally:
        def test_screenshot(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testscreenshot",
                      attachment_type=AttachmentType.PNG)

    def test_homepage(self):
        title1 = self.driver.title
        if title1 == "Event Plan On":
            print("logged in successfully")
            msg1 = datawritepass()
        else:
            msg2 = datawritefail()

    def test_eventdiary(self):
        eventdiary = eventdiarypage(self.driver)
        time.sleep(3)
        eventdiary.eventdiarytask().click()

    def test_tasktab(self):
        tasktab = tasktabpage(self.driver)
        time.sleep(6)
        tasktab.Taskpage().click()

    def test_kanbanview(self):
        kanbanview = Kanbanview(self.driver)
        time.sleep(3)
        kanbanview.addbutton().click()
        kanbanview.selecttask().click()
        kanbanview.statusselect().click()
        time.sleep(2)
        kanbanview.inprogress().click()
        time.sleep(3)
        kanbanview.priority().click()
        kanbanview.lowpriority().click()
        time.sleep(2)
        kanbanview.assigncontact().click()
        kanbanview.contactSelect().click()
        time.sleep(2)
        kanbanview.Contactclose().click()
        time.sleep(4)
        kanbanview.dateClick().click()
        time.sleep(2)
        kanbanview.Hourclear().clear()
        kanbanview.Hourvalue().send_keys("10")
        kanbanview.Minclear().clear()
        kanbanview.Minvalue().send_keys("00")
        time.sleep(2)
        kanbanview.Pmclick().click()
        time.sleep(3)
        kanbanview.Eventadd().send_keys('events')
        #time.sleep(2)
        #self.driver.find_element_by_xpath('//div[@class="btn btn-group"]//a[@ptooltip="Attach a File"]').click()
        #self.driver.find_element_by_xpath('//ul[@class="dropdown-menu dropdown-menu-right show"]//li[1]').click()
        #time.sleep(3)
        #self.driver.find_element_by_xpath('//p[@style="padding: 10px;"]//div[@class="dropzoneAlignMiddle col-12"]//dropzone//div[1]//div[1]//div[1]').send_keys('G:\\Thirdeye\\newformtext')
        time.sleep(3)
        kanbanview.kanbanclose().click()
        time.sleep(3)

    def test_listing(self):
        listing = Listingpage(self.driver)
        listing.listingbutton().click()
        listing.edittask().click()
        time.sleep(3)
        listing.prioritylevel().click()
        time.sleep(1)
        listing.inprogress().click()
        listing.Statusclick().click()
        time.sleep(3)
        listing.Statuslevel().click()
        listing.Assigncontact().click()
        time.sleep(1)
        listing.Contacclick().click()
        time.sleep(2)
        listing.Contactclose().click()
        time.sleep(4)
        listing.Addtag().send_keys('events')
        time.sleep(3)
        listing.Listingclose().click()
        time.sleep(2)

    def test_calendar(self):
        calendar = Calendarpage(self.driver)
        calendar.calendarclickbutton().click()
        actions = ActionChains(self.driver)
        click1 = calendar.dateclick()
        actions.double_click(click1).perform()
        time.sleep(3)
        calendar.levelclick().click()
        time.sleep(1)
        calendar.levelselect().click()
        calendar.statusclick().click()
        time.sleep(3)
        calendar.inprogress().click()
        time.sleep(3)
        calendar.assigncontact().click()
        time.sleep(1)
        calendar.Contactclick().click()
        time.sleep(2)
        calendar.Contactclose().click()
        time.sleep(3)
        calendar.Calendarclose().click()
        time.sleep(2)

    def test_eventtask(self):
        addnewevent = Addnewevent(self.driver)
        time.sleep(4)
        addnewevent.addnewbutton().click()
        addnewevent.eventname().send_keys('charity event')
        description = 'charity event oraganised many people'
        addnewevent.eventdesc().send_keys(description)
        addnewevent.Datebuttonclick().click()
        addnewevent.Dateselect().click()
        addnewevent.Timeclick().click()
        addnewevent.Timehourclear().clear()
        addnewevent.Timehourinsert().send_keys("09")
        addnewevent.Timeminclear().clear()
        addnewevent.Timemininsert().send_keys("00")
        addnewevent.Timepmclick().click()
        time.sleep(5)
        addnewevent.Selectstatus().click()
        time.sleep(3)
        addnewevent.inprogress().click()
        addnewevent.Priorityselect().click()
        time.sleep(1)
        addnewevent.mediumselect().click()
        addnewevent.assign_contact().click()
        time.sleep(1)
        addnewevent.assigncontactclick().click()













