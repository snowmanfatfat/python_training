import email.message as mes
msg=mes.EmailMessage() # 產生訊息物件
msg["From"]="zqq1559874@gmail.com" # 寄件人
msg["To"]="zqq1559874@gmail.com" # 收件人
msg["Subject"]="你好"
# msg.set_content("測試") # 純文字內容用set_content
msg.add_alternative("<h3>優惠券</h3>滿五百送一百", subtype="html") # 使用html語法讓內容豐富一點，h3是3號標題，會把字放大、行距拉開且是粗體

import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com", 465) # 到網路上查詢gmail smtp server的主機名稱跟port，連線到server
server.login("zqq1559874@gmail.com","tijhdumkwricwldp") # 帳號密碼，有開啟兩階段驗證的話就用應用程式密碼
server.send_message(msg)
server.close() # 關閉連線
