from subprocess import call
import os


def make_model_and_benchmark(fasttext_path, benchmark_path, file_path, thread):
    fasttext_path = os.path.abspath(fasttext_path)
    make_model_order = '/fasttext skipgram -input ' + file_path + ' -output ' + file_path.replace('.txt', '') + '_model ' + '-thread ' + thread
    call([fasttext_path + make_model_order], shell=True)
    benchmark_path = os.path.abspath(benchmark_path)
    benchmark_order = '/scripts/evaluate_on_all.py ' \
                      '-f ' + file_path.replace('.txt', '') + '_model.vec ' \
                      '-o '+ file_path.replace('.txt', '') +'_result.csv ' \
                      '-p word2vec'
    call([benchmark_path + benchmark_order], shell=True)


#TODO:
# 1. 각각의 파라미터를 입력받아 저장
# 2. 입력받은 파라미터에 대하여 입련한 값으로 프로그램 실행
