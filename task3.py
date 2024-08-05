import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the website
    driver.get('https://labour.gov.in/')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Download the Monthly Progress Report
    # Go to "Documents" menu
    documents_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[7]/ul/li[2]/a')))
    documents_menu.click()

    # Wait for the "Monthly Progress Report" link to be visible and clickable
    report_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Monthly Progress Report')))
    report_url = report_link.get_attribute('href')

    # Download the Monthly Progress Report
    response = requests.get(report_url)
    with open('Monthly_Progress_Report.pdf', 'wb') as file:
        file.write(response.content)

    print("Monthly Progress Report downloaded successfully.")

    # Download photos from Photo Gallery
    # Go to "Media" menu
    media_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Media')))
    media_menu.click()

    # Go to "Photo Gallery"
    photo_gallery_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Photo Gallery')))
    photo_gallery_menu.click()

    # Create a folder to save photos
    os.makedirs('Photo_Gallery', exist_ok=True)

    # Wait for the photos to load
    time.sleep(5)  # Adjust sleep time if necessary

    # Find all image elements
    images = driver.find_elements(By.TAG_NAME, 'img')

    # Download up to 10 images
    count = 0
    for img in images:
        if count >= 10:
            break

        src = img.get_attribute('src')
        if src:
            # Download the image
            response = requests.get(src)
            if response.status_code == 200:
                with open(f'Photo_Gallery/photo_{count + 1}.jpg', 'wb') as file:
                    file.write(response.content)
                print(f"Photo {count + 1} downloaded.")
                count += 1

finally:
    # Ensure the WebDriver quits
    driver.quit()
