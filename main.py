from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time


def main():
    chrome_driver_path = "/usr/lib/chromium-browser/chromedriver"
    cookie_clicker_url = "http://orteil.dashnet.org/experiments/cookie/"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(cookie_clicker_url)

    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
    store = driver.find_elements(By.CSS_SELECTOR, "#store b")
    purchased_items = []

    timeout = time.time() + 60 * 5  # 5 minutes from now

    cookie_icon = driver.find_element(By.ID, "cookie")
    while time.time() < timeout:
        # driver.implicitly_wait(1)
        cookie_icon.click()
        for item in store:
            if item.text.split(' ')[-1].replace(',', '').isdigit():
                price_item_digit = int(item.text.split(' ')[-1].replace(',', ''))
                if money >= price_item_digit and price_item_digit not in purchased_items:
                    purchased_items.append(item)
                    item.click()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
