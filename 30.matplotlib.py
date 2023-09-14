import matplotlib.pyplot as plt
# 折線圖
plt.plot([1,2,3],[2,4,4]) # matplotlib封包底下的pyplot模組的plot函數畫圖，輸入前面是x後面是對應的y
plt.show()

# 畫兩條線
"""
    第一組(2,4),(3,6),(4,8)
    第二組(2,2),(3,3),(4,4)
"""

# 使用rc方法(runtime configuration 執行階段的設定)，設定執行環境才能在圖表中表示中文
plt.rc("font",family="Microsoft JhengHei") # 把字型設定成微軟正黑體 (有支援中文的字型)

plt.plot(
    [2,3,4], 
    [[4,2],[6,3],[8,4]],
    label=["第一組","第二組"] # 繪圖時設定標籤
)
plt.legend() # 設定標籤後呼叫legend產生圖例
plt.xlabel("x軸標題")
plt.ylabel("y軸標題")
plt.show()

import csv
with open("data.csv", "r", encoding="utf-8") as file:
    reader=csv.reader(file)
    header=next(reader) # 讀取第一列當標頭
    x=[] # 年度
    y=[] # 薪水
    for data in reader:
        x.append(int(data[0])) # 記得做轉換
        y.append([int(data[1]), int(data[2])]) # 因為y是要放list所以要寫成list的樣子
    # x = [int(row[0]) for row in reader] 
    # y = [int(row[1]) for row in reader] 不能這樣寫，要在一個迴圈裡同時讀x和y才行，若分開，x讀完之後指標就到整個檔案的底部了，會讀不出y來

print(header)
print(x,"\n",y)
plt.plot(x,y,label=header[1:3])
plt.legend()
plt.xlabel(header[0])
plt.ylabel("薪水")
plt.show()

# 使用Pie方法根據一個維度的資料畫出圓餅圖
# plt.pie(x,labels=[str(100*x[0]/sum(x))+"%", 
#                   str(100*x[1]/sum(x))+"%", 
#                   str(100*x[2]/sum(x))+"%"],labeldistance=0.5) 

x=[10,15,25] # 用迴圈寫較簡潔
labels=[str(100*data/sum(x))+"%" for data in x]
plt.pie(x,labels=labels,labeldistance=0.5) 

# labeldistance用以設定標籤位置，0表圓心、1表圓周，也可大於1，表示在圓餅圖之外
# 自己算%，算完的數字轉成字串再加上%這個符號
plt.legend()
plt.title("123")
plt.show()

with open("pie.csv", "r", encoding="utf-8") as file:
    reader=csv.reader(file)
    next(reader) # 把第一列讀取掉，因為不需要
    x=[]
    labels=[]
    for row in reader:
        x.append(int(row[1]))
        labels.append((row[0]))
print(x,"\n",labels)
plt.pie(x,labels=labels)
plt.show()