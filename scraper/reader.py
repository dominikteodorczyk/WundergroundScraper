from selenium import webdriver
from datetime import datetime
import pandas as pd
from time import sleep

class SiteObject():

    def __init__(self, site_path, start, end):
        '''
        Klasa inicjalizująca object drive selenium
        '''
        self.site_path = site_path
        self.chromedriver = r'scraper\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.get(site_path)
        self.start = start
        self.end = end

    def getHistorySite(self):

        for i in self.driver.find_elements_by_class_name("ng-star-inserted"):
            href = str(i.get_attribute('href'))

            if href.startswith('https://www.wunderground.com/history/'):
                return href


    def getData(self):

        history_site = self.getHistorySite()
        all_data = pd.DataFrame()


        DateFrame = DaysURLs(self.start, self.end).getDaysList()
        for i in list(DateFrame):
            day_url = history_site + "/date/" + i.strftime("%Y-%m-%d").replace("-0","-")
            self.driver.get(day_url)
            table_object = self.driver.find_element_by_class_name('mat-column-dateString')
            
            sleep(1)
            print(table_object)



class DayPageExtractor():

    def __init__(self, day_url, driver:webdriver):
        self.url = day_url
        self.driver = driver.get(day_url)


    def getTableContent(self):

        table_object = self.driver.find_elements_by_class_name("mat-table cdk-table mat-sort ng-star-inserted")
        print(table_object)




class DaysURLs():

    def __init__(self, first_day, last_day):
        self.start = first_day
        self.end = last_day

    def getDaysList(self) -> list:

        return pd.date_range(self.start,self.end)
