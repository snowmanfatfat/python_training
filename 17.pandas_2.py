import pandas as pd
data=pd.read_csv("googleplaystore.csv") # 把csv檔案讀成dataframe
print(data.shape)
print(data.columns)
print(data["Rating"].mean()) # 4.19
print(data["Rating"].median()) # 4.3 中位數大於平均數，表示大部分偏高分但有人分數太低拉低平均
print(data["Rating"].nlargest(100).mean()) # 5.14? 超過5表示有問題 (前一百大應用程式的平均)
print(data[data["Rating"]>5]["Rating"]) # 找出奇怪資料並排除

condition=data["Rating"]<=5
datafiltered=data[condition]
print(datafiltered["Rating"].mean()) 
print(datafiltered["Rating"].median()) 
print(datafiltered["Rating"].nlargest(1000).mean())

# 觀察安裝數量，但他是用字串表達，要轉成數字，且資料有符號需清理
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
condition=data["Installs"]>100000
print(data[condition].shape) # 找出安裝數10萬以上的app有幾個
print(data[condition].shape[0]) # 找出的資料格式是tuple

# 基於資料做關鍵字搜尋
keyword=input("請輸入關鍵字:")
condition=data["App"].str.contains(keyword, case=False) # 可以忽略大小寫
print(data[condition]["App"])