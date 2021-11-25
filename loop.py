#$n = int(input("nhap gia trị tu ban phim: "))
#for i in range(0,n+1):
#    print(i)
n = int(input("nhap gia tri tu ban phim: "))
count = 0
while count <= n:
    print(count)
    count+=1
print("vậy giá trị nhập từ bán phím là: ",count)

for i in range(5 ,0 ,-1):
    for j in range(0 ,i ,-1):
        print(j, end = " ")
    print()

