#封包:包含模組的資料夾，用來整理分類模組程式，即檔案對應到模組，資料夾對應到封包
#-專案資料夾
#  -主程式.py
#  -封包資料夾(有裝__init__才是封包資料夾，沒有的話只是一般資料夾)
#     -__init__.py(做初始化，裡面可留空，python自己會產生這個檔案)
#     -模組一.py
#     -模組二.py

#import 封包.模組 as 模組名

import geometry1.point as point
#或寫成 from geometry1 import point 也可以

print(point.distance(3,4))

#但不能這樣寫:
# import geometry1 as gm
# print(gm.point.distance(3,4))
