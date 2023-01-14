from scraper.reader import SiteObject, DayPage
from time import sleep
from datetime import datetime

SiteObject('https://www.wunderground.com/weather/de/berlin/IBERLI1114').getHistorySite()
sleep(5)
