from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.hemnet.se/salda/bostader?location_ids%5B%5D=940808&item_types%5B%5D=villa&sold_age=6m')
time.sleep(5) # Let the user actually see something!

classElements = driver.find_elements_by_class_name('sold-results__normal-hit')

print(classElements)

#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()