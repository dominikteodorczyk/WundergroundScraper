from selenium import webdriver


class SiteObject():

    def __init__(self, site_path):
        '''
        Klasa inicjalizująca object drive selenium
        '''
        self.chromedriver = r'scraper\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromedriver)
        self.driver.get(site_path)

    def getHistorySite(self):

        for i in self.driver.find_elements_by_class_name("ng-star-inserted"):
            href = str(i.get_attribute('href'))
            print(href)
            if href.startswith('https://www.wunderground.com/history/'):
                print(href)
                i.click()