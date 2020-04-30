from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Optiion3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
