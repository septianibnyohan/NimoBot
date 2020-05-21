import time
from selenium import webdriver
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list


PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "proxyType":"MANUAL",
    
}

#data
link = "https://www.nimo.tv/emperor"

#setting
wait_second = 6

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
#driver.get('https://www.nimo.tv/')
driver.get(link)

btn_show_login = driver.find_element_by_css_selector(".reg-login-btn:nth-child(2) > .nimo-btn")
btn_show_login.click()

time.sleep(wait_second)

#input phone
txt_phone = driver.find_element_by_css_selector(".phone-number-input")
txt_phone.send_keys("85778151604")

#input password
txt_password = driver.find_element_by_css_selector(".c3-pl:nth-child(1)")
txt_password.send_keys("Nimoonline01")

#input login
btn_login = driver.find_element_by_css_selector(".nimo-login-body-button")
btn_login.click()

#driver.get(link)

#btn_play = driver.find_element_by_css_selector(".play")
#btn_play.click()


# time.sleep(wait_second);

# txt_comment = driver.find_element_by_css_selector(".nimo-room__chatroom__chat-box__input")
# txt_comment.send_keys("Saya subscribe bang youtubemu")
# btn_send_comment = driver.find_element_by_css_selector(".nimo-chat-box__send-btn")
# btn_send_comment.click()