import random
data=random.choice([1,5,6,10,20]) # choice是隨機選取一個值
data=random.sample([1,5,6,10,20],3) # sample是隨機選取n個值
data=[1,5,8,20]
random.shuffle(data) # 對data就地調換
data=random.random() # 取得0~1之間的隨機亂數
data=random.uniform(60,100) # 取得60~100之間的隨機亂數，且每個數字出現機率相等
data=random.normalvariate(100,10) #取得常態分配亂數，平均數100標準差10

import statistics as stat
data=stat.mean([1,4,5,8])
data=stat.median([1,4,5,8])
data=stat.stdev([1,4,5,8])
print(data)