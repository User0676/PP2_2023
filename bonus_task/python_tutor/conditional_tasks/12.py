n = int(input())
m = int(input())
k = int(input())

if n*m>=k:
    if k%n == 0:
        print("YES")
    elif k%m == 0:
        print("YES")
    else:print("NO")
else:print("NO")