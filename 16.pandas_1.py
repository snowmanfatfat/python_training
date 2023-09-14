# pandas就像試算表的資料分析套件，series單維以list為底、dataframe雙維以dic為底
import pandas as pd
data=pd.Series([20,10,15])
data.max()
data.median()
data*=2
data=data==20 # 把每一個元素都拿去比較

data=pd.DataFrame({
    "name":["a","b","c"],
    "salary":["1","2","3"]
})
data["name"] # 取得特定欄位
data.iloc[0] # 取得特定列，iloc是ilocation的意思

data=pd.Series([20,10,15], index=["a","b","c"]) #series已內建索引，但也可用自己的索引，要注意數量要和元素數量相同
data.dtype
data.size
data.index
data[2]
data["a"]
data.sum()
data.std()
data.nlargest(3) # 取前n大
data.prod() # 相乘

data=pd.Series(["Aa","Bb","Cc"])
data.str.lower() # 字串操作要在str底下，此處是轉為小寫
data.str.upper()
data.str.len() # 算出每個字串的長度
data.str.cat(sep=",") # 把字串用,串起來
data.str.contains("A") # 判斷字串中是否包含A
data.str.replace("Aa","Dd") # 把Aa換成Dd

data=pd.DataFrame({
    "name":["amy","bob","chris"],
    "salary":[1,2,3]
}, index=["a","b","c"])
data.shape
print("取得第一列",data.iloc[0], sep="\n") # 按照順序取列
print("取得第一列",data.loc["a"], sep="\n") # 按照索引取列，注意沒有i
# dataframe取得欄或列就是series了
names=data["name"]
names.str.upper()

#建立新欄位
data["Revenue"]=[10,20,30]
data["Rank"]=pd.Series([3,6,1], index=["a","b","c"]) # 因為前面自訂編號，所以這裡也要編號
data["cp"]=data["Revenue"]/data["salary"]

data=pd.Series([20,10,15])
condition=data>18 # 篩選是True的值
data[condition]

data=pd.Series(["Aa","Bb","Cc"])
condition=data.str.contains("A")
data[condition]

data=pd.DataFrame({
    "name":["amy","bob","chris"],
    "salary":[1,2,3]
})
# 在dataframe中的篩選都是針對列
condition=data["salary"]>=2
condition=data["name"]=="Amy"
print(data[condition])

