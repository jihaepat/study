kim_count = 0
lee_count = 0
jy_count = 0
count = 0
original_array =['이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌']
for i in range(len(original_array)):
    if original_array[i][0:1]=='김':
        kim_count+=1;
    elif original_array[i][0:1]=='이':
        lee_count+=1;
        if original_array[i]=='이재영':
            jy_count+=1;
print(' 김씨는 : ',kim_count ,'\n','이씨는 : ',lee_count,'\n','이재영 : ',jy_count)
set_array = list(set(original_array))
print(set_array)
sort_array = sorted(set_array)
print(sort_array)

