from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://baochinhphu.vn/tin-moi.htm")
print(driver.title)
item = driver.find_element(By.ID, "102231126120838945")
print(item)
# for titleH2 in items:
#     print("111111")
#     title = titleH2.text
#     print(title)
#     print("=================")

driver.close()