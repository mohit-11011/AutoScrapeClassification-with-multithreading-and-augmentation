import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import threading
import multiprocessing
from selenium.webdriver.chrome.options import Options
numberOfCores = multiprocessing.cpu_count()
activethreads=threading.active_count()
image_element_list={}
def image_element_fun(search):
    #if there is space it will add hiffen as url processes search que
    query=search.replace(" ", "-")
    url=f"https://unsplash.com/s/photos/{query}?license=free"
    #opens chrome
    chrome_options = Options()
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    try:
    # Wait for the "Load More" button to be clickable
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[4]/div[3]/div[1]/button')))
        #clicks load more button
        element.click()
    except Exception as e:
        print(f"An error occurred while clicking 'Load More': {str(e)}")
        driver.quit()
        image_element_fun(search)
        
    scroll_iterations = 5
    counter=0
    while(counter<scroll_iterations):
        actions = ActionChains(driver)
        current_scroll_position = driver.execute_script("return window.pageYOffset;")
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)  # Wait for the content to load
        new_scroll_position = driver.execute_script("return window.pageYOffset;")
        if new_scroll_position == current_scroll_position:
            actions.send_keys(Keys.PAGE_UP).perform()
            time.sleep(5)
        else:
            counter+=1
    #converts whole page into html text
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #closes the driver window
    driver.quit()
    #wait for soup to convert all page into html
    time.sleep(5)
    image_elements = soup.find_all("div", class_="MorZF")  # Find all <div> elements with class "morzf"
    del image_elements[:20]
    image_element_list[search]=image_elements
def multithreading_for_searches(searches):
    for search in searches:
        t = threading.Thread(target=image_element_fun , args=(search,))
        t.start()
    while True:
        if (threading.active_count()==activethreads):
            break
        time.sleep(1)
    return image_element_list

