# 網頁原始碼是由html格式撰寫而成，所謂爬蟲即爬取網頁html原始碼，而html是由許多標籤組成，標籤是網頁運作的基本單位
# html巢狀結構
# <html> <>就是一個標籤，結尾是</>，之間的文字叫內文
#     <head>
#         <title>HTML格式</title>
#     </head>
#     <body>
#         <div id="head">網頁結構簡介</div> div標籤後面的是標籤屬性
#         <div class="list">
#             <a class="item">連結文字一</a> a標籤表超連結
#             <a class="item">連結文字二</a>
#         </div>
#     </body>
# </html>

# 網頁爬蟲的基本流程:
# 1.指示selenium連線到特定網址
# 2.解析html架構，取得想要的標籤
# 3.針對標籤操作

# 取得滿足條件的一個標籤 WebElement
# driver.find_element(搜尋欄位,"搜尋條件")
# 取得滿足條件的所有標籤 WebElement list
# driver.find_elements(搜尋欄位,"搜尋條件")

# 根據標籤的class屬性搜尋標籤
# driver.find_elements(By.CLASS_NAME,"搜尋條件")

# 以上例而言即driver.find_elements(By.CLASS_NAME,"item")
# 會以list的形式取得兩個標籤
# [<a class="item">連結文字一</a>,
#  <a class="item">連結文字二</a>]

# 根據連結標籤的文字搜尋標籤
# driver.find_elements(By.LINK_TEXT,"搜尋條件")
# 以上例而言即driver.find_element(By.LINK_TEXT,"連結文字一")
# 會取得一個標籤<a class="item">連結文字一</a> (當只想要取一個標籤時可用文字搜尋，因為文字不太會重複)

# element=driver.find_element(搜尋欄位,"搜尋條件")
# 取得標籤後要取得標籤的內文
# elemen.text

# 取得標籤後要取得標籤的某個屬性
# element.get_attribute("屬性名稱")

# 模擬使用者點擊標籤
# element.click()

from selenium import webdriver
from selenium.webdriver.common.by import By # 引入By這個類別
from selenium.webdriver.chrome.options import Options
options=Options()
options.chrome_executable_path="C:\python_training\chromedriver.exe" 
driver=webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
#　print(driver.page_source) # 取得網頁原始碼

for i in range(3):
    tags=driver.find_elements(By.CLASS_NAME, "title")
    for tag in tags:
        print(tag.text)
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁") # 利用超連結標籤的內文去找到超連結
    link.click() # 模擬使用者點擊上頁連結標籤，可以爬更多頁

driver.close()


