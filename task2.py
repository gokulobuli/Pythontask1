from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:

    url = 'https://www.cowin.gov.in/'
    driver.get(url)


    faq_link = driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a")
    faq_link.click()


    partners_link = driver.find_element(By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
    partners_link.click()


    time.sleep(3)


    window_handles = driver.window_handles

    print("Window Handles:")
    for handle in window_handles:
        print(handle)


finally:
    driver.quit()
