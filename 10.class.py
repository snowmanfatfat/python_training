# class:封裝的函式或變數，統稱類別屬性(不是實體屬性)
class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("not supported")
        else:
            print("read from", src)
print(IO.supportedSrcs) #類別.類別屬性
IO.read("file")
IO.read("internet")

# 先定義類別，再透過類別建立實體物件，之後才能使用實體屬性
# class 類別名稱:
#     def __init__(self): 定義初始化函式，透過操作self來定義實體屬性
#     def 方法名稱(self, 更多自訂參數): 定義實體方法
#       方法主體,透過self操作實體物件，self表示這個方法所屬的實體物件
# obj=類別名稱() 呼叫初始化函式即可建立物件以及初始的實體屬性

class Point:
    def __init__(self, x, y):
        self.x=x # 把參數傳到實體屬性中，實體屬性是封裝在實體物件的變數，實體方法是封裝在實體物件中的函式
        self.y=y
    def show(self):
        print(self.x, self.y)
    def distance(self, targetX, targetY):
        return ((targetX-self.x)**2+(targetY-self.y)**2)**0.5

p=Point(3,4) # 呼叫初始化函式建立實體物件並取得實體屬性、實體方法
print(p.x, p.y) # 實體物件.實體屬性
p.show() #呼叫實體方法
print(p.distance(0, 0)) #計算(3,4)和(0,0)的距離

# 利用實體方法分割運算邏輯的狀況下，可能不太適合使用with open，因為這樣寫馬上就會關閉檔案，無法把動作分開處理
class File:
    def __init__(self, name):
         self.name=name
    def read(self):
        with open(self.name, mode="r", encoding="utf-8") as file:
            return file.read()
    def write(self, word):
        with open(self.name, mode="w", encoding="utf-8") as file:
            file.write(word)

# 用class可以簡化複雜的程式碼
f=File("data.txt")
print(f.read())
f.write("abc")
print(f.read())

#也可以寫成以下
class File:
    def __init__(self, name):
        self.name=name
        self.file=open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
    def write(self, word):
        with open(self.name, mode="w", encoding="utf-8") as file:
            file.write(word) #write比較特別，當用open選擇w時，檔案馬上會被覆蓋掉，若選擇r+，則是會新增資料
    def close(self):
        self.file.close() #也可不加close，反正程式結束時file自然關閉，除非是像web server這種跑很久的程式才要特別注意，關閉檔案用意是節省資源

f=File("data.txt")
print(f.read())
f.write("789")
f.close()