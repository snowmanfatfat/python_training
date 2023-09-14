#模仿switch的寫法
def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"
    
#一般if-else的寫法
age = 120
if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    "You're too young to party"

#不用寫break,已經內建了    
lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _: #_表示預設情況
        print("The language doesn't matter, what matters is solving problems.")

x=input("請輸入數字") #取得字串形式的使用者輸入
x=int(x) #將字串型態轉換成數字型態
if x>200:
    print("1")
elif x>100:
    print("2")
else:
    print("3")
    
y=input("請輸入數字") #取得字串形式的使用者輸入
y=int(y) #將字串型態轉換成數字型態
match y:
    case y if y>200: #看y有沒有符合這個case,而case後面也能再接條件
        print("1")
    case y if y>100:
        print("2")
    case _:
        print("3")
        
#四則運算
a=int(input("請輸入數字"))
b=int(input("請輸入數字"))
op=input("請輸入符號")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("NA")
        
a=int(input("請輸入數字"))
b=int(input("請輸入數字"))
op=input("請輸入符號")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("NA")
    
