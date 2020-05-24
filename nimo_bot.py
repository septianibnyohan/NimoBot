import time
import json
import urllib.request
import socket
import urllib.error
import pyautogui
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import csv

def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.nimo.tv')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        print("ERROR:", detail)
        return True
    return False


with open("config.json") as json_data_file:
    config = json.load(json_data_file)

user_list_file = 'userlist.csv'
users = []
with open(user_list_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=config["csv_delimiter"],lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['phone_number'] = row[0]
        user['password'] = row[1]
        users.append(user)

proxy_list_file = 'proxylist.csv'
proxies= []
with open(proxy_list_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=config["csv_delimiter"],lineterminator="\n")
    next(rows, None)
    for row in rows:
        proxy = {}
        proxy['proxy_address'] = row[0]
        proxy['port'] = row[1]
        proxy['username'] = row[2]
        proxy['password'] = row[3]
        proxies.append(proxy)

nimo_url = input('Input nimo url : ')

usr_index = 0
for usr in users:
    PROXY = proxies[usr_index]['proxy_address'] + ":" + proxies[usr_index]['port']
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "proxyType":"MANUAL"
    }
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(nimo_url)
    usr_index = usr_index + 1


# req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list() #this will create proxy list




#PROXY = proxies[0].get_address()
# print("country : ", proxies[0].country)
# #print("bad proxy : ", is_bad_proxy(PROXY))
# print("proxy : ",PROXY)

#PROXY = "103.22.248.59:61661"
# PROXY = "p.webshare.io:80"

# index_proxy = 0
# while proxies[index_proxy].country != "Indonesia":
#     index_proxy = index_proxy + 1

#     if proxies[index_proxy].country == "Indonesia":
#         PROXY = proxies[index_proxy].get_address()
#         if is_bad_proxy(PROXY):
#             index_proxy = index_proxy + 1

    # while is_bad_proxy(PROXY) :
    #     PROXY = proxies[index_proxy].get_address()
    #     #print("bad proxy : ", is_bad_proxy(PROXY))
    #     print("proxy : ",PROXY)
    #     index_proxy = index_proxy + 1

# PROXY = "202.158.1.12:8090"
#print("bad proxy : ", is_bad_proxy(PROXY))

# print("proxy : ",PROXY)

# webdriver.DesiredCapabilities.CHROME['proxy']={
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "proxyType":"MANUAL",
#     # 'class': "org.openqa.selenium.Proxy",
#     # 'autodetect': False,
#     # 'socksUsername': 'kglsyyfz-1',
#     # 'socksPassword': 'z134whxk1eo1'
# }

# with open("config.json") as json_data_file:
#     config = json.load(json_data_file)

# #data
# link = config["nimo_link"]
# comment = config["comment"]

# #setting
# wait_second = config["wait_second"]
# phone_number = config["login"]["phone_number_login"]
# password = config["login"]["password_login"]

# driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('https://www.expressvpn.com/what-is-my-ip')

# time.sleep(1)
# pyautogui.typewrite("kglsyyfz-1")
# pyautogui.press('tab')
# pyautogui.typewrite("z134whxk1eo1")
# pyautogui.press('enter')


# time.sleep(10)
# driver.quit()

# #PROXY="23.236.158.18:80"

# webdriver.DesiredCapabilities.CHROME['proxy']={
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "proxyType":"MANUAL",
#     # 'class': "org.openqa.selenium.Proxy",
#     # 'autodetect': False,
#     # 'socksUsername': 'kglsyyfz-1',
#     # 'socksPassword': 'z134whxk1eo1'
# }

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://httpbin.org/ip')

# pyautogui.typewrite("kglsyyfz-2")
# pyautogui.press('tab')
# pyautogui.typewrite("z134whxk1eo1")
# pyautogui.press('enter')

# alert=driver.switch_to_alert()
# time.sleep(3)
# alert.send_keys("kglsyyfz-1"+webdriver.common.keys.Keys.TAB+"z134whxk1eo1")
# alert.accept() 
#driver.get(link)

# btn_show_login = driver.find_element_by_css_selector(".reg-login-btn:nth-child(2) > .nimo-btn")
# btn_show_login.click()

# time.sleep(wait_second)

# #input phone
# txt_phone = driver.find_element_by_css_selector(".phone-number-input")
# txt_phone.send_keys(phone_number)

# #input password
# txt_password = driver.find_element_by_css_selector(".c3-pl:nth-child(1)")
# txt_password.send_keys(password)

# #input login
# btn_login = driver.find_element_by_css_selector(".nimo-login-body-button")
# btn_login.click()

# #driver.get(link)

# # #btn_play = driver.find_element_by_css_selector(".play")
# # #btn_play.click()


# time.sleep(wait_second)

# txt_comment = driver.find_element_by_css_selector(".nimo-room__chatroom__chat-box__input")
# txt_comment.send_keys(comment)
# btn_send_comment = driver.find_element_by_css_selector(".nimo-chat-box__send-btn")
# btn_send_comment.click()