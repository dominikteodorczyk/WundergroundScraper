from selenium import webdriver
from datetime import datetime


class SiteObject():

    def __init__(self, site_path, start, end):
        '''
        Klasa inicjalizująca object drive selenium
        '''
        self.chromedriver = r'scraper\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.get(site_path)
        self.start = start
        self.end = end

    def getHistorySite(self):

        for i in self.driver.find_elements_by_class_name("ng-star-inserted"):
            href = str(i.get_attribute('href'))
            print(href)
            if href.startswith('https://www.wunderground.com/history/'):
                print(href)
                i.click()

    def iteratorOfDays():
        pass

class DayPage():

    def __init__(self, date):
        self.date = date

    def strDateGenerator(self):

        return self.date.strftime("%Y-%m-%d")

    def hrfDayPage(sefl):

        return 

    