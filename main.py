import selenium.webdriver.common.by
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

chrome_driver_path = "C:/Users/drorlotan/PycharmProjects/development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
big_cookie = driver.find_element(By.ID, "bigCookie")

game_is_on = True
def click_cookie():
    while game_is_on:
        big_cookie.click()
def play_game():
    while game_is_on:
        time.sleep(5)
        products = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        try:
            products[-1].click()
        except:
            pass

def five_min():
    time.sleep(300)
    global game_is_on
    game_is_on = False


t1 = threading.Thread(target=click_cookie)
t2 = threading.Thread(target=play_game)
t3 = threading.Thread(target=five_min)
t1.start()
t2.start()
# t3.start()
