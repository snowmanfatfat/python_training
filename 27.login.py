# 取得標籤的方法
# 根據標籤的id
# driver.find_element(By.ID, "搜尋條件")

# 根據標籤的任意屬性(透過CSS選擇器)
# driver.find_element(By.CSS_SELECTOR, "[屬性名稱=屬性的值]")

# 模擬使用者輸入文字
# element=driver.find_element(搜尋欄位, "搜尋條件")
# element.send_keys("文字")

# 模擬使用者按下特定功能按鍵
# element.send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="C:\python_training\chromedriver.exe" 
driver=webdriver.Chrome(options=options)
driver.get("https://leetcode.com/accounts/login/")
time.sleep(5) # 進網頁後等登入畫面跑出來
account=driver.find_element(By.ID, "id_login") # 帳號輸入框
password=driver.find_element(By.ID, "id_password") # 密碼輸入框
botton=driver.find_element(By.ID, "signin_btn")
account.send_keys("snowmanfat")
password.send_keys("rgnmk1654")
password.send_keys(Keys.ENTER)
time.sleep(60) # 等待登入完成
driver.get("https://leetcode.com/problemset/all/")
time.sleep(3) # 等待頁面載入
problem=driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]") # 根據任意欄位搜尋標籤
print(problem.text) # 抓取個人解題紀錄
column=problem.text.split("\n") # 把字串根據換行符號切割，會形成一個list
print("刷題數量", column[1])