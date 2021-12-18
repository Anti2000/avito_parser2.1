from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random
#
#
# def login(username, password):
#     browser = webdriver.Chrome('chromedriver')
#     options = webdriver.ChromeOptions()
#     # options.add_argument("disable-blink-features=AutomationControlled")
#
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", True)
#
#     options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
#
#     options = options
#
#
#
#
#     try:
#         browser.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
#         # browser.switch_to.new_window('tab')
#         #
#         # browser.get('https://avito.ru/#login?authsrc=h')
#         # time.sleep(random.randrange(3, 5))
#         #
#         # username_input = browser.find_element_by_name('login')
#         # username_input.clear()
#         # username_input.send_keys(username)
#         #
#         # time.sleep(2)
#         #
#         # password_input = browser.find_element_by_name('password')
#         # password_input.clear()
#         # password_input.send_keys(password)
#         #
#         # password_input.send_keys(Keys.ENTER) WebDriver(New)	present (failed)
#         # time.sleep(10)
#         time.sleep(10)
#         browser.close()
#         browser.quit()
#     except Exception as ex:
#         print(ex)
#         browser.close()
#         browser.quit()
#
#
# login(username, password)

#############################################################################
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from auth_data import username, password
# import time
# import random
#
# print(password, username)
#
# login()
#
# def login(username, password):
#     browser = webdriver.geckodriver()
#
#     browser.get('https://m.avito.ru/#login?authsrc=h')
#     time.sleep(random.randrange(3, 5))
#
#     username_input = browser.find_element_by_name("login")
#     username_input.clear()
#     username_input.send_keys(username)
#
#     time.sleep(2)
#
#     password_input = browser.find_element_by_name("password")
#     password_input.clear()
#     password_input.send_keys(password)
#
#     password_input.send_keys(Keys.ENTER)
#     time.sleep(2)
#
#     browser.close()
#     browser.quit()

######################################################################



# if __name__ == "__main__":
#     login()
#     #main()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from data import username, password
# import time
# import random


# def login(username, password):
#     browser = webdriver.Chrome('../chromedriver/chromedriver')
#
#     try:
#         browser.get('https://www.instagram.com')
#         time.sleep(random.randrange(3, 5))
#
#         username_input = browser.find_element_by_name('username')
#         username_input.clear()
#         username_input.send_keys(username)
#
#         time.sleep(2)
#
#         password_input = browser.find_element_by_name('password')
#         password_input.clear()
#         password_input.send_keys(password)
#
#         password_input.send_keys(Keys.ENTER)
#         time.sleep(10)
#
#         browser.close()
#         browser.quit()
#     except Exception as ex:
#         print(ex)
#         browser.close()
#         browser.quit()
#
#
# login(username, password)


from selenium import webdriver
import time


# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

# disable webdriver mode

# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="chromedriver",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")



    driver.switch_to.new_window('tab')
    driver.get('https://avito.ru/#login?authsrc=h')
    time.sleep(random.randrange(3, 5))
    username_input = driver.find_element_by_name('login')
    #username_input = driver.find_element('login')
    username_input.send_keys(username)
    time.sleep(2)

    password_input = driver.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)

    print(username, password)

    time.sleep(30)
except Exception as ex:
    print(ex, 'error')
finally:
    time.sleep(30)
    driver.close()
    driver.quit()

