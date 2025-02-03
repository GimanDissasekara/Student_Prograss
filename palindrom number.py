x = int(input("Enter the Number :"))
y,z=0,0
while x != 0 :
    y = x // 10
    z = x % 10
    x = y
    print(z,end=" ")
