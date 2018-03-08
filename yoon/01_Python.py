import re

chage_line =[]
text_line =  '	(탭)처음 라인입니다	(탭)처음라인 중간입니다\n						(탭)(탭) 두번째 라인 입니다	(탭)두번째라인 중간입니다\n	(탭)마지막 라인 입니다'
for i in re.finditer('\n	',text_line):
    j = 1
    while text_line[int(i.start())+j] == '	':
        chage_line.append(i.start()+j)
        j +=1
for j in range(-1:0)
