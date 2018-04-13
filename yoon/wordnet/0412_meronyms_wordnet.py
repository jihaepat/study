from nltk.corpus import wordnet

"""
1. 입력받은 단어를 -> 상의어 하의어로 매칭후 -> CSV 파일로 저장

1.1 입력받은 단어를 -> 입력받은 텍스트를 읽는다 -> 읽은 텍스트를 -> 단어로 나누어 배열로 가지고 있는다 -> 배열에 순서대로 for 구문을 돌리고 ->
순차적으로 하의어 상의어로 변환후 배열에 저장한다 -> 배열에 저장한 데이터를 CSV 형식에 맞게 저장한다

1.2 배열 길이가 너무 길어지는 문제가 발생 메모리 문제가 있을수 있음 -> 부분 저장을 하여 메모리를 초기화 후 계속 진행하는 방식으로 변경

1.3 입력받은 단어를 유사어로 분리시 이것도 데이터로 넣어야하는지 wordeveluation
"""
text_data_list =[]

hyponyms_list = []
hypernyms_list = []
synsets_list = []
text_file = open('./test_text.txt', 'r')
text_data = text_file.read()
text_data_list = text_data.split(', ')
for i in range(len(text_data_list)): #처음 입력받은 데이터
    for x in range(len(wordnet.synsets(text_data_list[i]))): # 입력받은 데이터를 유사어로 분리한 데이터
        print(text_data_list[i], ',', wordnet.synsets(text_data_list[i])[x].lemmas())

