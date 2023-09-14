#模組:一個獨立的程式檔案，先載入模組再使用其中的函式或變數
#sys模組:取得系統相關資訊
import sys
print(sys.platform) #印出作業系統
print(sys.maxsize) #印出整數型態的最大值
print(sys.path) #印出模組的搜尋路徑，載入模組時會按照這些路徑順序搜尋模組，模組必須放在這些路徑之中

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)