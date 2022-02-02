l = str(input("Input some comma seprated numbers : "))
li = l.split(',')
tup = tuple(li)

print('Tuple : ',tup)

sum=0

for i in range(0, len(tup)) :
    sum+=(int)(tup[i])

print('Sum of tuple elements : ',sum)
