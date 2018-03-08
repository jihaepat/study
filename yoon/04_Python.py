array_count=0
min_data=0
arraylist =[]
str_arr = input().split(' ')
arr = [int(i) for i in str_arr]
array_count =len(arr)
for j in range(array_count-1):
    arraylist.append(int(arr[int(j)+1])-int(arr[j]))
min_data =min(arraylist)
for j in range(len(arraylist)):
    if min_data == arraylist[j]:
        print("[",arr[j],",",arr[int(j)+1],"]")