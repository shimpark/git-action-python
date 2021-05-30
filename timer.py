# import module
from selenium import webdriver
import time

# Create the webdriver object. Here the
# chromedriver is present in the driver
# folder of the root directory.
driver = webdriver.Chrome("C:\GitHubs\chromedriver_win32\chromedriver.exe")

# get https://www.geeksforgeeks.org/
driver.get("https://www.gg-onestore.com/Font/FontTest")

# Maximize the window and let code stall
# for 10s to properly maximise the window.
driver.maximize_window()
time.sleep(2)

# Obtain button by link text and click.
button = driver.find_element_by_link_text("게임 START")
button.click()

time.sleep(0.01)
button = driver.find_element_by_link_text("아끼면 똥 된다")
button.click()

time.sleep(0.02)
button = driver.find_element_by_link_text("잘된 꼴 보기 좋다")
button.click()

time.sleep(0.04)
button = driver.find_element_by_link_text("얼레리 꼴레리")
button.click()

time.sleep(0.06)
button = driver.find_element_by_link_text("아끼면 똥 된다")
button.click()

time.sleep(0.09)
button = driver.find_element_by_link_text("잘된 꼴 보기 좋다")
button.click()

time.sleep(0.4)
button = driver.find_element_by_link_text("얼레리 꼴레리")
button.click()

time.sleep(0.5)
button = driver.find_element_by_link_text("아끼면 똥 된다")
button.click()

time.sleep(0.7)
button = driver.find_element_by_link_text("잘된 꼴 보기 좋다")
button.click()

time.sleep(0.92)
button = driver.find_element_by_link_text("얼레리 꼴레리")
button.click()


time.sleep(0.99)
button = driver.find_element_by_link_text("아끼면 똥 된다")
button.click()

time.sleep(1)
button = driver.find_element_by_link_text("잘된 꼴 보기 좋다")
button.click()

time.sleep(1.001)
button = driver.find_element_by_link_text("얼레리 꼴레리")
button.click()

time.sleep(1.35)
button = driver.find_element_by_link_text("아끼면 똥 된다")
button.click()

time.sleep(1.81)
button = driver.find_element_by_link_text("잘된 꼴 보기 좋다")
button.click()

time.sleep(2.9)
button = driver.find_element_by_link_text("얼레리 꼴레리")
button.click()
