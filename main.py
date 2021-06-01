from selenium import webdriver
import os
from openpyxl import Workbook


chromedriver = "C:\\Users\\tiwar\\Downloads\\chromedriver_win32\\chromedriver.exe"
os.environ ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
# webdriver.chrome(chromedrivermanager().install())
# driver.maximum_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[contains(@id, 'search')]").send_keys("Samsung phones")
driver.find_element_by_xpath("//input[@value='Go']").click()
driver.find_element_by_xpath("//span[text()='Samsung']").click()
phonenames = driver.find_elements_by_xpath("//span[contains(@class,' a-color-base a-text-normal')]")
prices = driver.find_elements_by_xpath("//span[contains(@class, 'a-price-whole')]")

myphone = []
myprice = []

for p in phonenames:
    myphone.append((p.text))

for p in prices:
    myprice.append(p.text)

data = zip(myphone, myprice)
finaldata = list(data)


wb = Workbook()
wb['Sheet'].title = 'Amazon Samsung Data'
sh1 = wb.active
sh1.append(['Name', 'Price'])

for x in finaldata:
    sh1.append(x)

wb.save("FinalRecords.xlsx")

driver.quit()

