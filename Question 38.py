num = input('Enter space separated numbers. \n')
t1 = tuple(int(x) for x in num.split())

l= len(t1)
print("The distinct pair whose product is even are.\n")
for i in range(l-1):
    j= i+1
    for k in range(j, l):
        if t1[i]*t1[k]%2==0:
            print(f"({t1[i]},{t1[k]})", end=', ')