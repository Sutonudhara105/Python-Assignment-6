num = input('Enter space separated numbers. \n')
t1 = tuple(int(x) for x in num.split())

count =[]
for ele in t1:
    c1= t1.count(ele)
    count.append(c1)

s= list(set(t1))
i= len(s)

for j in range(i):
    print(f"the element {s[j]} is present {count[j]} times.")
