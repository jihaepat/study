import time
# start_time = time.time()
minus_array=[]

number_array = input().split(' ')
for i in range(len(number_array)):
    if int(number_array[i]) < 0:
        minus_array += number_array[i]
        print(number_array[i])
print(minus_array[1])
# end_time =time.time() -start_time

# print(end_time)