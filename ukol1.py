def triangle(n):
    for n in range(2,n+1):
        for i in range(n):
                for j in range(n-i-1):
                    print(end=" ")
                for j in range(i+1):
                    print("X", end=" ")
                print()
        print(" ")     


n = int(input("Your number: "))
if n <= 11:
    triangle(n)
else :
    print("Write a less number!!!")