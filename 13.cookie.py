# cookie:網站存放在使用者瀏覽器的一小段內容，連線時放在request headers中送出
import urllib.request as req
def getdata(url):
    # 單純把網址改成八卦版會抓不到，因為有一個是否未滿18歲的確認頁面，點過之後會有一個over18的變數存在cookie中，
    # 但如果沒有給這個cookie就不會進到網頁裡面了，application->cookie (觀察連線如何進行並模仿)
    request=req.Request(url, headers={
    "cookie":"over18=1", #network->index.html->requset headers->cookie,告訴ptt已經按過了
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as rep: 
        data=rep.read().decode("utf-8")
        
    #抓取該頁面的所有文章標題
    import bs4 
    root=bs4.BeautifulSoup(data, "html.parser")
    #print(root.title.string) 
    titles=root.find_all("div", class_="title")
    #print(titles)
    for title in titles:
        if title.a != None:
            print(title.a.string)

    # 想要透過抓取上一頁的超連結來抓取更多網頁內容，首先在"上頁"按右鍵->檢查，可發現上頁的超連結，再透過觀察發現，應該要透過"上頁"這兩個字來抓到超連結
    nextlink=root.find("a", string="‹ 上頁") # 找到內文是上頁的a標籤
    #print(nextlink["href"])
    return "https://www.ptt.cc"+nextlink["href"] #因為nextlink是相對位址所以要補上前面的網址

url="https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(3): #想抓三頁
    url=getdata(url)

# 也可以這樣寫
count=0
while count<3:
    url=getdata(url)
    count+=1