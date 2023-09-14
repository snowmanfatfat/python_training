# syntax error:語法錯誤
# exception:程式可以執行，但某些情況會出現錯誤
# exception handling:事先預想可能發生的例外去處理，使程式不要中斷

while True: # 使用while True搭配break就可以使得發生錯誤時，讓使用者再重新輸入
    data=input("輸入數字")
    try:
        number=int(data) # 把可能會發生例外的程式碼放在這(因為input若是文字就無法轉換成int)
        break
    except Exception: # except後面接例外種類，此處接Exception表示接受各種例外
        print("格式錯誤") # 若上述try區塊的程式發生例外會跳進此區塊中的程式繼續執行，若正常則會跳過except

number=number*2
print(number)