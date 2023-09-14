# import urllib.request as req
# url="https://www.ptt.cc/bbs/movie/index9716.html"
# with req.urlopen(url) as rep:
#     data=rep.read().decode("utf-8")
# print(data) 會失敗，因為這個連線不像一般使用者，會被網頁伺服器拒絕

import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index9716.html"

# 開啟網頁按f12再重新整理，找到network->選all->index...html(找時間最長的那個檔案)->headers->
# request header->User-Agent
# 建立一個Request物件，附加Headers的資訊，這樣看起來才像使用者，尤其是user-agent會告訴伺服器用的是甚麼瀏覽器、os
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
})
with req.urlopen(request) as rep: # 要用request做urlopen
    data=rep.read().decode("utf-8")

# 解析原始碼萃取文章標題(要觀察標題在原始碼中的特色)
import bs4 # 專門拿來解析html檔案的套件
root=bs4.BeautifulSoup(data, "html.parser")
print(root.title.string) # 抓到網頁標題的文字
titles=root.find_all("div", class_="title") # 從網頁中尋找標籤div，篩選條件為title
print(titles) # 是一個列表
for title in titles:
    if title.a != None: # 有些文章若被刪除就不會有a了所以用if
        print(title.a.string) #因為標題在a後面
