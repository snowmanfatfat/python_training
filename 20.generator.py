# generator:動態產生可疊代的資料，搭配for迴圈(因為generator本身也是一個可疊代的資料)
def test():
    print("階段一")
    yield 5 # 使用yield建立生成器，且yield可以寫很多個
    print("階段二")
    yield 10
gen=test() # 呼叫函式後就會回傳生成器(不是5)，只要函式中有yield，呼叫函式時不會執行裡面的程式碼
for data in gen: # for迴圈去看def的程式碼，往下執行遇到第一個yield是5就回傳5
    print(data)

# 產生偶數數列
def generateEven(maxnumber):
    number=0
    while number<=maxnumber: # 若用 while True就可產生無窮個數列，再用for迴圈控制break即可
        yield number
        number+=2
        
for data in generateEven(10): # 進到程式碼中，遇到yield即放入data，再回到函式中繼續執行尋找yield
    print(data)