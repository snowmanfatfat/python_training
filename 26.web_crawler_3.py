# JS程式:在瀏覽器中可執行的程式語言，用來控制瀏覽器或操作網頁

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="C:\python_training\chromedriver.exe" 
driver=webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
for i in range(3): # 看要捲動幾次
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") # 利用selenium模組在瀏覽器執行javascript程式做更細部的網頁操作，此為捲動視窗至底部
    time.sleep(2) # 等待2秒讓瀏覽器有時間載入新滑動到的資料，不然若滑至底部就馬上抓會抓不到新的 
tags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for tag in tags:
    print(tag.text)
driver.close()