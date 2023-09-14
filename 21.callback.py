# callback:透過參數來傳遞函式到另一個函式中
def test(arg):
    arg(1000) # 呼叫callback func，帶入參數

def handle(x):
    print(x)
    
test(handle)

def add(x, y, n): # 這樣寫的好處是add就專門做加法，其他輸出格式由callback func決定，且想更換不同格式時只要更換func即可
    n(x+y)

def handle1(result):
    print("結果是",result)
    
def handle2(result):
    print("result is", result)

add(5,6,handle2)