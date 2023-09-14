# 讀取json格式(儲存一些設定檔、或是在網路交換資料的格式)
# import json
# 讀取的資料=json.load(檔案物件)

# json.dump(要寫入的資料,檔案物件)

# with open(檔案路徑, mode=開啟模式) as 檔案物件
#  讀取或寫入檔案的程式
# 以上區塊會自動、安全的關閉檔案

with open("data.txt", mode="w", encoding="utf-8") as file: # 開啟檔案時可以順便編碼
    file.write("5\n3")

with open("data.txt", mode="r", encoding="utf-8") as file:
    sum=0
    for data in file: #把檔案中的數字一行行讀取並加總
        sum+=int(data)
print(sum)

import json
with open("config.json", mode="r") as file:
    data=json.load(file)
print(f'name: {data["name"]}\nversion: {data["version"]}') # json用字典在儲存資料

data["name"]="New name" # 修改變數中的資料
with open("config.json", mode="w") as file: # 把最新資料寫回檔案
    json.dump(data, file)
    