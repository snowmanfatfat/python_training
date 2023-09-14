# AJAX:網頁在背景透過JavaScript程式發出請求
# 有些網站不像ptt是伺服器直接回傳有資料的html檔，而是會給不帶資料的html檔，瀏覽器再根據回傳的檔案利用AJAX技術再跟伺服器要資料
# 這種網站特徵有:通常看原始碼找不到原本網站上顯示的標題等文字，以及重新整理時會先出現空白畫面才出現內容，不像ptt是馬上更新
# 有時候只寫User-Agent沒辦法騙過伺服器，要多寫一點headers
# 爬取kkday產品標題
import urllib.request as req
# 用開發人員工具的XHR尋找含有標題的東西(用preview觀察，preview是有經過分類，而response是原始回傳值)->找到ajax_get_homepage_setting->發現是json格式 搞定了
# 從headers的request url可以找到真正含有資料的網址
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=273791a87a18b2ebe6fabccb02f6cf9e"
request=req.Request(url, headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding":"gzip, deflate, br" 不要寫這個，這句話的意思是本地接收壓縮格式的數據，服務器傳過來壓縮格式gzip的文件，而解壓這種gzip文件只能用deflate算法，瀏覽器能夠自動解壓，python卻不能自動解壓，需要額外進行設置才行，會使decode utf-8失效
    "Accept-Language":"zh-TW,zh;q=0.9,en;q=0.8",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})
with req.urlopen(request) as rep: # 要用request做urlopen
    data=rep.read().decode("utf-8")

import json
data=json.loads(data)
# 直接看preview的格式就很清楚架構為何
# 因為看格式得知list的第2項以後變成字典格式，所以要分開處理
data_list=data["data"]["homepage_product_group"][:2]
data_dic=data["data"]["homepage_product_group"][2:]

for i in data_list:
    for j in i["prod_list"]:
        print(j["name"])

for i in data_dic:
    for j in i["prod_list"]:
        print(i["prod_list"][j]["name"])  #印出所有dic中key對應的value值
        
# 爬蟲:了解網頁採用甚麼技術、尋找正確的網址、正確地和網站伺服器互動的方式、資料清理