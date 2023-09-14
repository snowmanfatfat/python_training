# numpy:用陣列代替列表處理資料，適合處理多維度數值運算，也是pandas(資料處理)、tensorflow(機器學習)的基礎，運算速度遠高於原生的list，因為底層用c、c++在運作
import numpy as np
ndarr=np.array([3,4,5]) # 用list建立ndarray物件(n個dimention陣列的意思即多維陣列)
print(ndarr)
print(ndarr.size)

np.empty(3) # 建立資料未指定的一維陣列，有三個空間但資料不確定(維持原本記憶體的位置有的東西)
np.zeros(3) # 建立三個資料都是0的一維陣列
np.ones(3) # 建立三個資料都是1的一維陣列
np.arange(10) # 建立0~9的一維陣列

print(np.array([[1,2],[3,4],[5,6]])) # 建立3X2的二維陣列，第一層3個第二層2個
np.empty([3,2])
np.zeros([3,2])
np.ones([3,2])

print(np.array([
    [[5,2,4],[1,2,8]],  
    [[3,8,2],[4,1,3]]
]))

np.empty([2,2,3])
np.zeros([3,1,3])

np.array([ # 創造一個1X1X2X3的四維陣列
    [
        [
            [1,2,3],
            [4,5,6]
        ]
    ]
])

# 逐元運算(elementwise):針對array中的每個資料逐一進行基本運算，兩個陣列的shape要一樣
data1=np.array([3,4,1])
data2=np.array([-2,5,-8])
data1*data2 #也可以+,-,/,>,>=,==

# 矩陣運算(matrix)
data1=np.array([[1,2]]) # 1X2
data2=np.array([[3,2,0],[3,1,-1]]) #2X3
data1.dot(data2) # 內積 1X3
data1@data2 # 內積
print(np.outer(data1,data2)) # 外積 2X6 (第一個矩陣2、第二個矩陣6，所以2X6)，會把1乘上所有值放在第一列，2乘上所有值放在第二列

# 統計運算，都可代入axis=...去指定維度  
data2.sum()
data2.sum(axis=0) # 加總第一個維度，若以table來看就是column
data2.sum(axis=1) # 加總第二個維度，若以table來看就是row
data2.min()
data2.cumsum() # 逐值累加 cumulate，即第i筆資料是第1~i筆資料的總和
data2.mean()
data2.std()

# 維度:資料的層次 形狀:同時表達資料的層次和每個層次的資料數量
# 原始資料是8個數字，可以表達成不同形狀
[1,2,3,4,5,6,7,8] # (8,) 一維陣列

[
    [1,2,3,4],
    [5,6,7,8]
] # (2,4) 二維陣列

data=np.array([
    [
        [1,2],[3,4]
    ],[
        [5,6],[7,8]
    ]
]) # (2,2,2) 三維陣列
data.shape
data.T.shape # 轉置:形狀反過來，1X2X3變成3X2X1，但維度不變
data.ravel() # 把資料打平成一維陣列，但原始資料不受影響，這函數是回傳一個新的陣列
data.reshape(4,2) # 改變形狀但資料數量需一樣，但原始資料不受影響，這函數是回傳一個新的陣列
data=np.zeros(18).reshape(2,3,3) # 資料初始化常用0
data=np.arange(9).reshape(3,3) # 產生數值0~8的3X3陣列

a=np.array([[1,2,3],[4,5,6],[7,8,9]]) # 第一個紫色框是第一維,第二個藍色框是第二維,是3X3的二維矩陣，沒逗號,所以都是對第一維操作

# indexing，索引取值，表示單一的值
print("a=", a[1,2])

# slicing，把原本陣列切片，表示多個值，配合indexing操作
print("a=", a[:]) # 全取
print("a=", a[1:])
print("a=", a[:1])
print("a=", a[1:2])

# 要對不同維度操作就加上逗號區隔 (用f'文字{變數}'就可把文字和變數寫在一起)
print(f'a={a[1, :]}') # 第一維取第1個，第二維全取
print(f'a={a[:, 1]}') # 第一維全取，第二維取第1個
print(f'a={a[:, 1:]}') # 第一維全取，第二維從第1個開始取
print(f'a={a[1:][:, 1:]}') # 第一維從第1個開始取，再把取出來的矩陣的第一維全取，第二維從第1個開始取，和原本相比即變成去掉第一行第一列的矩陣

b=np.array([
    [
        [1,2,3],[4,5,6]
    ],
    [
        [7,8,9],[10,11,12]
    ]
])
print("b=", b[1, ...]) # ...表全都要
print("b=", b[...,1])
print("b=", b[...,1:3])

# stacking(合併)
arr1=np.array([
    [1,2,3],
    [4,5,6]
]) # 2X3
arr2=np.array([
    [7,8,9],
    [10,11,12]
]) # 2X3
arr3=np.array([
    [13,14,15],
    [16,17,18]   
]) # 2X3
print(np.vstack((arr1,arr2,arr3))) # 合併第一個維度，第二個維度不動，把要合併的陣列用tuple裝起來，(2+2+2)X3->6X3
print(np.hstack((arr1,arr2,arr3))) # 合併第二個維度，2X(3+3+3)->2X9

"""
    三個雙引號可以拿來當多行註解，裡面的東西不影響程式
"""

# splitting:把一個陣列切割成很多陣列

arr=np.array([
    [2,4,6,8,10,12],
    [1,3,5,7,9,11]
]) # 2X6
print(np.vsplit(arr,2)) # 對第一個維度切割，即橫著切開變成2個(2/2)X6->1X6的陣列
print(np.hsplit(arr,3)) # 對第二個維度切割，即直著切開變成3個2X(6/3)->3X3的陣列(左中右各一群)


