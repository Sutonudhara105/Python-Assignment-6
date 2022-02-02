tup = tuple(map(int,input("Please Input Numbers: ").split()))
uni = [] 
rep = []
for x in tup:
    if x in uni:
        rep.append(x)
    else:
        uni.append(x)

print('Tuple : ',tup)
print('Unique Elements :',uni)
print('Duplicate Elements :',rep)
