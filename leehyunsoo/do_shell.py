from subprocess import call
import os


def make_model_and_benchmark(fasttext_path, benchmark_path, file_path, thread):
    fasttext_path = os.path.abspath(fasttext_path)
    make_model_order = '/fasttext skipgram -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                  '') + '_model ' + '-thread ' + thread
    call([fasttext_path + make_model_order], shell=True)
    benchmark_path = os.path.abspath(benchmark_path)
    benchmark_order = '/scripts/evaluate_on_all.py ' + '-f ' + file_path.replace('.txt',
                                                                                 '') + '_model.vec ' + '-o ' + file_path.replace(
        '.txt', '') + '_result.csv ' + '-p word2vec'
    call([benchmark_path + benchmark_order], shell=True)

    return file_path.replace('.txt', '')


def make_model_and_benchmark2(fasttext_path, benchmark_path, file_path, **kwargs):
    thread = kwargs.get('thread')
    model = kwargs.get('model')
    fasttext_path = os.path.abspath(fasttext_path)
    if model != None:
        assert model=='cbow'
        make_model_order = '/fasttext'+model+' -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                      '') + '_model '
    else :
        make_model_order = '/fasttext skipgram -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                          '') + '_model '

    if thread != None:
        assert int(thread)
        make_model_order += '-thread ' + thread



    call([fasttext_path + make_model_order], shell=True)
    benchmark_path = os.path.abspath(benchmark_path)
    benchmark_order = '/scripts/evaluate_on_all.py ' + '-f ' + file_path.replace('.txt',
                                                                                 '') + '_model.vec ' + '-o ' + file_path.replace(
        '.txt', '') + '_result.csv ' + '-p word2vec'
    call([benchmark_path + benchmark_order], shell=True)
    return file_path.replace('.txt', '')


assert os.listdir(
    make_model_and_benchmark('/home/leehyunsoo/work/fastText',
                             '/home/leehyunsoo/work/word-embeddings-benchmarks',
                             '/media/leehyunsoo/4TB2/usa_patent/small_claims.txt', '6')) \
       == \
       os.listdir(
           make_model_and_benchmark2('/home/leehyunsoo/work/fastText',
                                     '/home/leehyunsoo/work/word-embeddings-benchmarks',
                                     '/media/leehyunsoo/4TB2/usa_patent/small_claims.txt', '6'))

# TODO:
# 1. 각각의 파라미터를 입력받아 저장
# 2. 입력받은 파라미터에 대하여 입련한 값으로 프로그램 실행


# FastText Default값
# input,                    : 불러올 데이터
# model = "skipgram",       : 훈련할 model의 종류 [skipgram, cbow]
# lr = 0.05,                :
# dim = 100,                :
# ws = 5,                   :
# epoch = 5,                : 데이터 처음부터 끝까지 훈련을 돌리는 횟수
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
