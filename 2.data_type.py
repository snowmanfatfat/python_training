1//2 #只留商數的除法

2**3 #次方

2**0.5 #開根號

7%3 #取餘數

x=1
x+=1 #x=x+1

#字串格式(要用"還是'都可以)
"hell\"o" #在"前面加上\就可以使"被印出
"hello\nworld" #\n表換行
"""hello

world""" #三個"就可以直接換行，且換幾行都會被印出來
"hello"*3 #複製三遍

#字串串接
"hello"+"world"
"hello" "world"

#對字串中的字元操作
s="hello"
print(s[1:4])
print(s[1:])
print(s[1])
print(s[:4])
print(s.replace("hello","")) #取代字串

#list操作
grades=[12,60,15,70,90]
grades[1:4]=[] #連續刪除
grades=grades+[12,33] #加入列表資料

#巢狀列表
data=[[3,4,5],[6,7,8]]
data[0][0:2]=[5,5,5]

#集合運算
s1={3,4,5}
3 in s1 #判斷元素有無在集合中
10 not in s1
s2={4,5,6,7}
s1&s2 #交集
s1|s2 #聯集
s1-s2 #差集
s1^s2 #反交集

s=set("hello") #將字串拆解成不重複且順序不一的集合

dic={"apple":"蘋果","bug":"蟲子"}
dic["apple"]
"apple" in dic #判斷key是否存在
del dic["apple"] #刪除字典中的key-value pair

#可以用列表的資料產生字典
dic={x:x*2 for x in [3,4,5]} 
print(dic)