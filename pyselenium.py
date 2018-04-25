from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/iah/Desktop/unitTestingCourse/day2/chromedriver')
driver.get("http://www.google.com")
elem = driver.find_element_by_id("lst-ib")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)




searchDivs = driver.find_elements_by_class_name("rc")
print len(searchDivs)

firstResult = driver.find_element_by_class_name('r')
firstResult.click()


if driver.title == "PyCon 2018 in Cleveland, Ohio | May 9-17":
	print "The page with the same target as expected : "  + driver.title

driver.close()
