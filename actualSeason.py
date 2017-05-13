import urllib2
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome('/Users/emilnamen/Downloads/eng-england-master/chromedriver')
driver.get("http://www.bbc.com/sport/football/premier-league/results")

# elem = driver.find_element_by_id("tournament-page-results-more")
# elem.click()
# elem.click()
# elem.click()

#tableScores = driver.find_element_by_xpath('//table[@class=\'soccer\']')

rows = driver.find_elements_by_class_name("match-details")  # get all of the rows in the table
for row in rows:
    cols = r

    # try:
    #     element = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'odd stage-finished'))
    #         )
    #     try:
    #         print element.text
    #     except StaleElementReferenceException as e:
    #         print e
    #         pass
    # finally:
    #     driver.quit()
    # cols = row.find_elements_by_tag_name("td")
    # for col in cols:
    #    print col.text  # prints text from the element
