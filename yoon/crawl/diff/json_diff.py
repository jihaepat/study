import os
import datetime
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_END     = "\033[0m"

prnt_date = datetime.datetime.now().strftime('%Y%m%d%H%M')
ipnavi_path = '/media/yoonjae/4TB2/ScrapyData'
if len(os.listdir(ipnavi_path)) < 2:
    print('비교대상이 없습니다.')
dirs_new = os.listdir(ipnavi_path)[-1]
dirs_old = os.listdir(ipnavi_path)[-2]
print('이전파일 :',C_RED+dirs_old+C_END)
print('최신파일 :', C_GREEN+dirs_new+C_END)

os.system('diff /media/yoonjae/4TB2/ScrapyData/'+dirs_old+' /media/yoonjae/4TB2/ScrapyData/'+dirs_new+' > /media/yoonjae/4TB2/diffData/shangbiao_diff_'+prnt_date+'.json')
file = open('/media/yoonjae/4TB2/diffData/shangbiao_diff_'+prnt_date+'.json', 'r', encoding='utf-8')
while True:
    line = file.readline()
    if not line:
        break
    if line[0:1] == '>':
        print(C_GREEN+' 추가'+C_END, '상호 :', line[line.find('"name": ')+8:line.find(', "cat"')], '등록번호 :', line[line.find('"register_num": ')+16:line.find(', "stable_num": ')], '공고번호: ', line[line.find('"stable_num": ')+14:line.find(', "status": ')])
    elif line[0:1] == '<':
        print(C_RED+' 삭제'+C_END, '상호 :', line[line.find('"name": ')+8:line.find(', "cat"')], '등록번호 :', line[line.find('"register_num": ')+16:line.find(', "stable_num": ')], '공고번호: ', line[line.find('"stable_num": ')+14:line.find(', "status": ')])