from selenium import webdriver
from datetime import datetime
import pandas as pd
from time import sleep, time
from decimal import Decimal

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
        all_data = pd.DataFrame(columns=['time', 'temp', 'dew_point', 'hum', 'wind', 'wind_speed', 'wind_gust', 'press', 'precip', 'condition'])


        DateFrame = DaysURLs(self.start, self.end).getDaysList()
        for i in list(DateFrame):
            start= time()
            dzien = i.strftime("%Y-%m-%d").replace("-0","-")
            day_url = history_site + "/date/" + dzien
            self.driver.get(day_url)
            sleep(1)

            day_data = pd.DataFrame(columns=['time', 'temp', 'dew_point', 'hum', 'wind', 'wind_speed', 'wind_gust', 'press', 'precip', 'condition'])

            for i in range(1,25):
                day_data = day_data.append({
                    'time': self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[1]/span").text,
                    'temp' : float(format(((int(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[2]/lib-display-unit/span/span[1]").text) - 32) * (5/9)),".2f")),
                    'dew_point' : float(format(((int(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[3]/lib-display-unit/span/span[1]").text) - 32) * (5/9)),".2f")),
                    'hum' : float(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[4]/lib-display-unit/span/span[1]").text),
                    'wind' : self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[5]/span").text,
                    'wind_speed' : float(format((1.609344*int(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[6]/lib-display-unit/span/span[1]").text)),".2f")),
                    'wind_gust' : float(format((1.609344*int(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[7]/lib-display-unit/span/span[1]").text)),".2f")),
                    'press' : float(format((float(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[8]/lib-display-unit/span/span[1]").text)),".2f")),
                    'precip' : float(format((float(self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[9]/lib-display-unit/span/span[1]").text)),".2f")),
                    'condition' : self.driver.find_element_by_xpath(f"//table/tbody/tr[{i}]/td[10]/span").text
                    },ignore_index = True)

            all_data = all_data.append(day_data)

        all_data.to_csv('test.csv', mode='w')


class DayPageExtractor():

    def __init__(self, day_url, driver:webdriver):
        self.url = day_url
        self.driver = driver.get(day_url)


    def getTableContent(self):

        table_object = self.driver.find_elements_by_
        print(table_object)




class DaysURLs():

    def __init__(self, first_day, last_day):
        self.start = first_day
        self.end = last_day

    def getDaysList(self) -> list:

        return pd.date_range(self.start,self.end)
