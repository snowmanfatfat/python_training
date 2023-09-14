import csv
with open("data.csv", "w", newline="") as file: # newline=""是為了避免最後多出一些空白
    writer=csv.writer(file) # 建立writer物件放入writer變數
    writer.writerow([1,2,3]) # 寫入一列的資料
    writer.writerow([4,5,6])
    writer.writerow([7,8,9])
    
with open("data.csv", "r", newline="") as file:
    reader=csv.reader(file)
    total=0
    for row in reader: # 逐行讀取，row是list結構，且元素都為字串形式
        for data in row: # 取出list中每一個字串
            total+=int(data)

print(total)