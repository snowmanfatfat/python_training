# decorator:是特殊設計的函式，用來輔助其他的函式
# def 裝飾器名稱(回呼函式名稱):
#     def 內部函式名稱():
#         裝飾器內部程式碼
#         回呼函式名稱()
#     return 內部函式名稱

def calculate1to50(cb):
    def run():
        result=0
        for n in range(51):
            result+=n
        cb(result) # 把計算結果透過參數傳遞到被裝飾的普通函式中
    return run

# 使用裝飾器，執行流程是先執行裝飾器的程式碼(即1加到50)，再執行cb函數(即show)，這樣做的好處是讓程式碼變得簡潔，把計算和顯示結果分開了
@calculate1to50
def show(x): # 注意此處的x是由裝飾器(即calculate1to50)計算完的結果傳過來的
    print("計算結果是",x)
    
@calculate1to50
def showEng(x):
    print("result is",x)

# 當呼叫帶有裝飾器的函數時，函數會被丟到裝飾器的cb裡面
show()
showEng()

# decorator factory:用來生產裝飾器的函式
# def 裝飾器工廠名稱(參數名稱,...):
#     def 裝飾器名稱(回呼函式名稱):
#         def 內部函式名稱():
#             裝飾器內部程式碼
#             回呼函式名稱()
#         return 內部函式名稱
#     return 裝飾器名稱

# 就像函式呼叫一樣，是在呼叫裝飾器工廠這個函式去產生裝飾器，再回傳裝飾器來使用，用途是可以處理額外的參數，要記得加()

def myFactory(base):
    def myDeco(cb):
        def run():
            print("裝飾器內的程式",base) # 裝飾器可以調用裝飾器工廠傳遞的參數
            result=base*2
            cb(result)
        return run
    return myDeco

@myFactory(3)
def show(x):
    print("普通函式的程式",x)

show() 

def calculate(base):
    def myDeco(cb):
        def run():
            result=0
            for n in range(base+1):
                result+=n
            cb(result)
        return run
    return myDeco

@calculate(100)
def show(x):
    print("累加是",x)

show()