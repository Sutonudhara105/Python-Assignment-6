l = str(input("Input some comma seprated numbers : "))
li = l.split(',')
tup = tuple(li)

print('Tuple : ',tup)

# Average of tuple 
sum = 0
for sub in tup:
	for i in sub:
		sum = sum + (int)(i)
res = sum / len(tup)

# printing result
print("The mean of tuple is : " + str(res))
