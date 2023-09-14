# iterable:可疊代，表可以分開、逐一取出內部資料的東西
# 例如字串、list、tuple、dictionary、set
# for 變數名稱 in 可疊代資料:
#  將可疊代的資料分開逐一取出
# 內建函式: max(可疊代資料)、sorted(可疊代資料)->不管當初給甚麼資料型態都回傳排序後的列表
for x in {"a", "b", 3, 10}:
    print(x) # 集合沒有順序性所以不會照著印
    
for x in "abc":
    print(x)

for x in {"a":3, "b":5}:
    print(x) # 字典是針對key值去跑

dic={"a":3, "b":5}
for x in {"a":3, "b":5}:
    print(dic[x]) # 要印出value必須這樣做
    
max("azu")
max({10,20,30,40})
max({"a":3, "b":5})

sorted("azu")
sorted({10,2,100,-5})