# import urllib.request as req
# src="https://www.ntu.edu.tw/"
# with req.urlopen(src) as response:
#    data=response.read().decode("utf-8") #取得台大網站的原始碼(前端)(HTML、CSS、JS)

#讀取台北市內科廠商名錄api
import json
import urllib.request as req
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire&limit=1000&offset="
data_list = [] # 每次api上限只能讀1000筆(政府規定)，總共5646筆，所以要用迴圈把所有資料讀進空字串中(limit每次位移1000筆)
for i in range(6):
    with req.urlopen(src+str(i*1000)) as response:
        data = json.load(response) # api是json資料格式
        data_list.append(data)

data_list[0]["result"]["results"][0]        
# 將公司名稱寫入檔案(可參照上述進行迴圈撰寫)
with open("company.txt", "w", encoding="utf-8") as file:
    for i in data_list: # 總共讀取次數
        for j in i["result"]["results"]: # 每次讀取的1000筆資料
            file.write(j["公司名稱"]+"\n")

# data_list完整樣貌如下表
[
    {"result":
        {"limit":1000,"offset":0,"count":5646,"sort":"","results":
            [
                {"_id":1,"_importdate":{"date":"2023-07-04 11:19:10.390210","timezone_type":3,"timezone":"Asia\/Taipei"},"統編":"00726398","公司名稱":"圓藝企業股份有限公司","公司地址":"114臺北市內湖區基湖路35巷49號","addr_x":"307146","addr_y":"2774694"},
                {"_id":2,"_importdate":{"date":"2023-07-04 11:19:10.399154","timezone_type":3,"timezone":"Asia\/Taipei"},"統編":"01183554","公司名稱":"合全產品開發股份有限公司","公司地址":"114臺北市內湖區瑞光路478巷18弄32號8樓","addr_x":"307272","addr_y":"2774611"},
                ...,
                {...}
            ]
        }
    }, # 讀一次1000筆如上述，隨著offset移動，把新讀到的資料再append進來date_list
    ...,
    {...} # 所以共讀6次，總共有6個{}
]

print(len(data_list))
# 是一個list，item數=讀取次數，本處讀6次故6個item，每個item是一個字典
[{"result":{"limit":1000,"offset":0,"count":5646,"sort":"","results":[...]}}, ... ,{"result":...}]

print(len(data_list[0]))
# 是一個字典，表示讀取第一次時的資料
{"result":{"limit":1000,"offset":0,"count":5646,"sort":"","results":[...]}}

print(len(data_list[0]["result"]))
# 是一個字典，表示api裡共有5個變數，limit、offset、count、sort、results
{"limit":1000,"offset":0,"count":5646,"sort":"","results":[...]}

print(len(data_list[0]["result"]["results"])) 
# 是一個list，每個item以字典形式儲存，item數即一次讀取的資料數，本處為1000
[{"_id":1,"_importdate":{"date":"2023-07-04 11:19:10.390210","timezone_type":3,"timezone":"Asia\/Taipei"},"統編":"00726398","公司名稱":"圓藝企業股份有限公司","公司地址":"114臺北市內湖區基湖路35巷49號","addr_x":"307146","addr_y":"2774694"},
 {"_id":2,"_importdate":{"date":"2023-07-04 11:19:10.399154","timezone_type":3,"timezone":"Asia\/Taipei"},"統編":"01183554","公司名稱":"合全產品開發股份有限公司","公司地址":"114臺北市內湖區瑞光路478巷18弄32號8樓","addr_x":"307272","addr_y":"2774611"},
 ...,
 {...}
]

print(len(data_list[0]["result"]["results"][0]))
# 是一個字典，每個item中共有_id、_importdate、統編、公司名稱、公司地址、addr_x、addr_y共7個變數
{"_id":1,"_importdate":{"date":"2023-07-04 11:19:10.390210","timezone_type":3,"timezone":"Asia\/Taipei"},"統編":"00726398","公司名稱":"圓藝企業股份有限公司","公司地址":"114臺北市內湖區基湖路35巷49號","addr_x":"307146","addr_y":"2774694"}

print(data_list[5]["result"]["results"][645]["_id"]) #輸出最後一筆資料的id