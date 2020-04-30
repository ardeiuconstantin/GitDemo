import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
list = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.implicitly_wait(10)
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons =driver.find_elements_by_xpath("//div[@class='product-action']/button")

for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list)


driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements_by_css_selector("p.product-name")
print(len(veggies))
for veg in veggies :
    list2.append(veg.text)

print(list2)

assert list[0] == list2[0]
assert list[1] == list2[1]
assert list[2] == list2[2]

originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountAmount) < float(originalAmount)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum1 = 0
for amount in amounts:
    sum1 = sum1 + int(amount.text)

print(sum1)

totalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert sum1 == totalAmount


