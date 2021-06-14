L1 = [1,3,5,7,9]
L2 = [2,4,6,8,10,12,14]

len1 = len(L1)
len2 = len(L2)

if len1 > len2:
    loopcnt = len1
else:
    loopcnt = len2

L3 = []
print (loopcnt)

for i in range(loopcnt):
    print (i)
    if i < len1:
        L3.append(L1[i])
    if i < len2:
        L3.append(L2[i])

print (L3)

