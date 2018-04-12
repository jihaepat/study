import os, sys

# os.system(
#     'fastText/fasttext skipgram -input /media/leehyunsoo/4TB2/usa_patent/small_claims.txt -output /media/leehyunsoo/4TB2/usa_patent/small_model')
# os.system(
#     'word-embeddings-benchmarks/scripts/evaluate_on_all.py -f /media/leehyunsoo/4TB2/usa_patent/small_model.vec -o /media/leehyunsoo/4TB2/usa_patent/result.csv -p word2vec')

from fastText import FastText


def make_model(data_file_path, data_file_name, save_file_name):
    # 로드할 data 파일의 경로 생성
    data_file_path = os.path.abspath(data_file_path)

    # 파일입력시 확장자 미입력의 경우 추가
    if not data_file_name.endswith('.txt'):
        data_file = data_file_path + '/' + data_file_name + '.txt'
    else:
        data_file = data_file_path + '/' + data_file_name

    # model을 저장할 파일의 경로 생성
    save_path = os.path.abspath(data_file_path) + '/' + save_file_name

    # TODO :사용자가 model 입력하하도록 매개변수 추가 예정

    # unsupervised model 생성시 기본 model은 skipgram임
    # 기타 default값은 아래에 기재

    try:
        model = FastText.train_unsupervised(data_file)
        # 불러온 data의 위치에 바로 저장(원본소스 수정으로 bin 과 vec 파일 자동 생성) -> 추후 변동 가능
        
        model.save_model(save_path)

    except Exception as e:
        print(e)
    return data_file


def benchmark(filepath):
    return filepath


assert make_model('/home/leehyunsoo/study', 'small_claims.txt',
                  'ttt') == '/home/leehyunsoo/study/small_claims.txt'
# assert make_model('/home/leehyunsoo/study/', 'ttt.csv', '') == '/home/leehyunsoo/study/ttt.csv'


# FastText Default값
# input,                    : 불러올 데이터
# model = "skipgram",       : 훈련할 model의 종류 [skipgram, cbow]
# lr = 0.05,                :
# dim = 100,                :
# ws = 5,                   :
# epoch = 5,                :
# minCount = 5,             :
# minCountLabel = 0,        :
# minn = 3,                 : 최소 n gram
# maxn = 6,                 : 최대 n gram
# neg = 5,                  :
# wordNgrams = 1,           :
# loss = "ns",              : 훈련방식의 차이 [ns, hs, softmax] 각각 어떤거로 하여도 결과값은 같은걸 확인하였으나 추가 확인이 필요함
# bucket = 2000000,         :
# thread = 12,              : 훈련시 사용할 thread개수
# lrUpdateRate = 100,       :
# t = 1e-4,                 :
# label = "__label__",      : 데이터안에 라벨링이 되어있는경우 라벨의 이름(기준점?)
# verbose = 2,              :
# pretrainedVectors = "",   :
