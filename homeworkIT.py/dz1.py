n = input().split()
array = [int(x) for x in n]
ar_n = []

for i in range (1,len(array)):
    if array[i]-array[i-1] !=1:
        ar_n.append(i)
if not ar_n:
    print("Не найдено")
else:
    print (ar_n)

