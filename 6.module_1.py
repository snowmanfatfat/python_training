import sys
sys.path.append("module") #新增當前資料夾底下的路經，因為geometry模組存在module資料夾裡，所以要新增路徑才找的到
import geometry
print(geometry.distance(1,1,5,5))