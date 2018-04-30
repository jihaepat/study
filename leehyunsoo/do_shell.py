from subprocess import call
import os


def make_model_and_benchmark(fasttext_path, benchmark_path, file_path, thread):
    fasttext_path = os.path.abspath(fasttext_path)
    make_model_order = '/fasttext skipgram -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                  '') + '_model ' + '-thread ' + thread
    call([fasttext_path + make_model_order], shell=True)

    benchmark_path = os.path.abspath(benchmark_path)
    benchmark_order = '/start_scripts/evaluate_on_all.py ' + '-f ' + file_path.replace('.txt',
                                                                                 '') + '_model.vec ' + '-o ' + file_path.replace(
        '.txt', '') + '_result.csv ' + '-p word2vec'
    call([benchmark_path + benchmark_order], shell=True)

    return file_path.replace('.txt', '')


def make_model_and_benchmark2(fasttext_path, benchmark_path, file_path, **kwargs):
    # 각각의 파라미터
    thread = kwargs.get('thread')
    model = kwargs.get('model')
    epoch = kwargs.get('epoch')
    dim = kwargs.get('dim')
    ws = kwargs.get('ws')

    fasttext_path = os.path.abspath(fasttext_path)

    if model != None:
        assert model == 'cbow'
        make_model_order = '/fasttext' + model + ' -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                          '') + '_model '
    else:
        make_model_order = '/fasttext skipgram -input ' + file_path + ' -output ' + file_path.replace('.txt',
                                                                                                      '') + '_model '

    if thread != None:
        assert int(thread)
        make_model_order += '-thread ' + thread

    call([fasttext_path + make_model_order], shell=True)

    benchmark_path = os.path.abspath(benchmark_path)
    benchmark_order = '/start_scripts/evaluate_on_all.py ' + '-f ' + file_path.replace('.txt',
                                                                                 '') + '_model.vec ' + '-o ' + file_path.replace(
        '.txt', '') + '_result.csv ' + '-p word2vec'
    call([benchmark_path + benchmark_order], shell=True)
    return file_path.replace('.txt', '')


def new_model_and_benchmark(fasttext_path, ft_input, fr_output, benchmark_path, bc_input, bc_output, **modelkwargs, ):
    assert os.path.isfile(ft_input) == True
    # assert os.path.isdir(os.path.abspath(output)) == True
    fasttext_path = os.path.abspath(fasttext_path)
    # make_model_order = '/fasttext skipgram -input /media/leehyunsoo/4TB2/small_data/half_half_abstract.txt -output /media/leehyunsoo/4TB2/model/half_abstract/half_half_abstract_epoc_5_ws_5 -thread 5'

    model = modelkwargs.get('model')

    if model == 'cbow':
        make_model_order = fasttext_path + '/fasttext' + model + ' -input ' + ft_input + ' -output ' + fr_output
    else:
        make_model_order = fasttext_path + '/fasttext skipgram -input ' + ft_input + ' -output ' + fr_output

    for key in modelkwargs.keys():
        if not key == 'model':
            make_model_order += '-' + key + ' ' + modelkwargs.get(key)

    call([make_model_order], shell=True)

# TODO:
# 1. 각각의 파라미터를 입력받아 저장
# 2. 입력받은 파라미터에 대하여 입련한 값으로 프로그램 실행


# FastText Default값
# input,                    : 불러올 데이터
# model = "skipgram",       : 알고리즘 종류 [skipgram, cbow]
# lr = 0.05,                :
# dim = 100,                :
# ws = 5,                   :
# epoch = 5,                : 데이터 처음부터 끝까지 훈련을 돌리는 횟수
# minCount = 5,             :
# minCountLabel = 0,        :
# minn = 3,                 : 최소 n gram
# maxn = 6,                 : 최대 n gram
# neg = 5,                  :
# wordNgrams = 1,           : 단어의 n gram
# loss = "ns",              : [ns, hs, softmax]가 있지만 기본 ns만 사용
# bucket = 2000000,         :
# thread = 12,              : 훈련시 사용할 thread개수
# lrUpdateRate = 100,       :
# t = 1e-4,                 :
# verbose = 2,              :
