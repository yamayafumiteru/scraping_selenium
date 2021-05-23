#coding: UTF-8
import time
import selenium
import chromedriver_binary
from selenium import webdriver

driver = webdriver.Chrome() # WebDriverのインスタンスを作成
driver.get('') # URLを指定してブラウザを開く

driver.find_element_by_id("google-auth-link").click()

login_id = "loginid"
login_pw = "pass"

#最大待機時間（秒）
wait_time = 30

### IDを入力
login_id_xpath = '//*[@id="identifierNext"]'
# xpathの要素が見つかるまで待機します。
driver.find_element_by_xpath(login_id_xpath).click()
driver.find_element_by_name("identifier").send_keys(login_id)
# 1秒待機
time.sleep(1)

next_btn_xpath = '//*[@id="identifierNext"]/div/button'
next_btn = driver.find_element_by_xpath(next_btn_xpath)
next_btn.click()
# 3秒待機
time.sleep(3)

### パスワードを入力
login_pw_xpath = '//*[@id="passwordNext"]'
# xpathの要素が見つかるまで待機します。
driver.find_element_by_xpath(login_pw_xpath).click()
driver.find_element_by_name("password").send_keys(login_pw)

# 1秒待機
time.sleep(1)
next_btn_login_xpath = '//*[@id="passwordNext"]/div/button'
next_btn_login = driver.find_element_by_xpath(next_btn_login_xpath)
next_btn_login.click()
'''
# 1秒待機
time.sleep(1)

# 次へボタンをクリック
time.sleep(1)
# パスワードを入力
password = driver.find_element_by_name("passwd")
password.send_keys("パスワードを入力")
#ログインボタンをクリック
login_btn = driver.find_element_by_name("btnSubmit")
login_btn.click()
'''