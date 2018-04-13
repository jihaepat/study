from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
def func_synsets():
    wn.synsets('dog')
    wn.synsets('dog', pos=wn.VERB)
    wn.synset('dog.n.01').definition()
    ret_synsets = wn.synset('dog.n.01')
    return ret_synsets

def func_similarity():
    dog = wn.synset('dog.n.01')
    cat = wn.synset('cat.n.01')
    ret_similar = dog.fun_similarity(cat)
    return ret_similar

def func_morpy():
    ret_morpy = wn.morphy('denied', wn.VERB)
    return ret_morpy

def func_synset_closures():
    dog = wn.synset('dog.n.01')
    hypo = lambda s: s.hyponyms()
    ret_closures = list(dog.closure(hypo, depth=1)) == dog.hyponyms()
    return ret_closures

# print(func_synsets())
# print(func_similarity())
# print(func_morpy())
# print(func_synset_closures())



"""
유의어(synsets)            : 비슷한 뜻을 가진 단어 출력
보조어(lemmas)             : 단어의 부명제
상위어(hypernyms)          : X가 Y의 한 종류이면 Y는 X의 상위어이다
하위어(hyponyms)           : Y가 X의 한 종류이면 Y는 X의 하위어이다
전체어(holonyms)           : X가 Y의 부분이면 Y는 X의 전체어이다
(verb_frame)              :
유사도(similarity)         : 단어간 비슷한 정도
(Access_to_all_Synsets)   : 해당 식에 맞는 단어 검색
(Morphy)                  : 단어의 형태소를 변환


동사의 분사(participle of verb)
파생된 형용사(root adjectives)
 : 단어에 대한 설명을 출력
synsets.lemmas : 단어의 부명제
synsets.hypernyms : 상위어
.member_holonyms : 동의어
.root_hypernyms : 최상단 상위어
.lowest_common_hypernyms() : 가장 낮은 상위 등위어
Similarity :
fun_similarity : 두 단어간 유사도
Access to all Synsets : 모든 단어를 검색
Morphy : 단어가 어떤 형태인지
wn.morphy('denied', wn.VERB)
Synset Closures : 단어와 단어사이 유사도

"""







