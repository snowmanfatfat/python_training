#1+2+3+...+10
n=1
sum=0
while n<=10:
    sum+=n
    n+=1
print(sum)

sum=0    
for x in range(11):
    sum+=x
else:
    print(sum) #最後跳出迴圈前印出加總的數字

n=1
while n<5:
    if n==3:
        break #跳出迴圈
    print(n)
    n+=1
print("最後的n",n) #可以用逗號隔開要印的東西

n=0
for x in [0,1,2,3]:
    if x%2==0: #x是偶數
        continue #直接執行下一圈
    print(x)
    n+=1
print("最後的n",n)

n=1
while n<5:
    print(n)
    n+=1
else:
    print(n) #else表示結束迴圈前做的事
    
for c in "hello":
    print(c)
else:
    print(c)

#找出整數平方根
n=int(input("請輸入數字"))
x=0
while x<=n:
    if x**2==n:
        print(x)
        break
    x+=1
else:
    print("na")
    
for i in range(n):
    if i**2==n:
        print(i)
        break #用break強制結束迴圈時,不會執行else
else:
    print("na")
