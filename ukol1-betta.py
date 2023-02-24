def triangle(n):
    for n in range(2,n+1):
        for i in range(1,n+1):
                for j in range(1,2*n):
                    if i==n or i+j==n+1 or j-i==n-1:
                        print("X", end=" ")
                    else:
                        print(" ", end=" ")
                print()
        print(" ")     


n = int(input("Your number: "))
if n <= 11:
    triangle(n)
else :
    print("Write a less number!!!")