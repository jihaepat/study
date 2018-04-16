from nltk.corpus import wordnet

"""
1. 입력받은 단어를 -> 상의어 하의어로 매칭후 -> CSV 파일로 저장

1.1 입력받은 단어를 -> 입력받은 텍스트를 읽는다 -> 읽은 텍스트를 -> 단어로 나누어 배열로 가지고 있는다 -> 배열에 순서대로 for 구문을 돌리고 ->
순차적으로 하의어 상의어로 변환후 배열에 저장한다 -> 배열에 저장한 데이터를 CSV 형식에 맞게 저장한다

1.2 배열 길이가 너무 길어지는 문제가 발생 메모리 문제가 있을수 있음 -> 부분 저장을 하여 메모리를 초기화 후 계속 진행하는 방식으로 변경

1.3 입력받은 단어를 유사어로 분리시 이것도 데이터로 넣어야하는지

** 4.13: wordnet.similarity 를 활용해서 평가(evaluation)


hyponyms_list = []
hypernyms_list = []
synsets_list = []

synset_insert = 0
result_insert = 0
text_file_read = open('./read_text.txt', 'r')


def text_hyponyms():
    text_data_list = text_file_read.read().split(', ')
    for i in range(len(text_data_list)):#처음 입력받은 데이터
        for x in range(len(wordnet.synsets(text_data_list[i]))):# 입력받은 데이터를 유사어로 분리한 데이터
            if wordnet.synsets(text_data_list[i])[x].hyponyms() != '[]':
                synset_insert = (wordnet.synsets(text_data_list[i])[x].hyponyms())
                for y in range(len(synset_insert)):
                    result_insert = text_data_list[i], synset_insert[y]
                    hyponyms_list.append(result_insert)


    return text_file_write.write(str(hyponyms_list))

def all_synset_load():
    for w in wordnet.all_synsets:
        print(w)
    return 1

all_synset_load()

hyponyms Synset('entity.n.01') : Synset('abstraction.n.06')0.6666666666666666,
hyponyms Synset('entity.n.01') : Synset('physical_entity.n.01')0.6666666666666666,
hyponyms Synset('entity.n.01') : Synset('thing.n.08')0.6666666666666666,

"""


def extract_relations_from_synset(synset):# synsets에서 받은 데이터를 변환한다
    # synsets, lemmas, hypernyms, hyponyms, holonyms,
    # similarity
    print()
    return [
        ['amphibious_landing.n.01', 'hypernyms', 'landing.n.04', 0.1],
        ['amphibious_landing.n.01', 'hypernyms', 'military_action.n.01', 0.1],
    ]


def format_relations_for_output(relations):
    result = []
    for r in relations:
        result.append('{} {} {} {}'.format(*r))
    return result


def make_wordnet_data_for_training():
    i = 0
    for synset in wordnet.all_synsets(): 
        relations = extract_relations_from_synset(synset)
        # print(relations)
        formatted = format_relations_for_output(relations)
        # for line in formatted:
            # print(line)

        i += 1
        if i > 10:
            break


make_wordnet_data_for_training()
