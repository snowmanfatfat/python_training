# selenium:用來做瀏覽器自動化的套件，是一個瀏覽器模擬工具，可以做網頁截圖、爬蟲、自動化測試
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 有一個options的類別可以創造物件
options=Options()
options.chrome_executable_path="C:\python_training\chromedriver.exe" # 在左邊檔案按右鍵選copy path即可，設定chrome driver的執行檔路徑(要透過driver去操控瀏覽器)
driver=webdriver.Chrome(options=options) # 建立driver物件實體，用程式打開瀏覽器
driver.maximize_window() # 視窗最大化
driver.get("https://www.google.com/") # 連線到google網頁
driver.save_screenshot("screenshot.png") # 做網頁截圖，檔名為a
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screenshot2.png")
driver.close()
