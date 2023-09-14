def total_sum(n):
    sum=0
    for x in range(n+1):
        sum+=x
    return sum

print(total_sum(100)) #呼叫函式回傳return後面的資料

def divide(n1,n2):
    print(n1/n2)
divide(n2=4,n1=2) #也可以直接指定參數的位置

#不定參數資料，參數前面加上*，會把參數變成tuple型態傳遞
def avg(*number):
    sum=0
    for x in number:
        sum+=x
    return sum/len(number)

print(avg(3,4,5))