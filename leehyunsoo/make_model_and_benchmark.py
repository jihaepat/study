import os, sys
from time import strftime


# os.system(
#     'word-embeddings-benchmarks/scripts/evaluate_on_all.py -f /media/leehyunsoo/4TB2/usa_patent/small_model.vec -o /media/leehyunsoo/4TB2/usa_patent/result.csv -p word2vec')


from fastText import FastText


def make_model(data_path, data_file_name, save_path, save_file_name, **kwargs):
    total_data_path = os.path.join(data_path, data_file_name)
    total_save_path = os.path.join(save_path, save_file_name)

    assert os.path.isfile(total_data_path) == True
    start_time = strftime("%y%m%d-%H%M%S")
    print('모델생산 시작시간 : ', start_time)

    try:
        if kwargs.keys() == None:
            model = FastText.train_unsupervised(total_data_path)
        else:
            model = FastText.train_unsupervised(total_data_path, **kwargs)

        model.save_vectors(total_save_path)

    except Exception as e:
        print(e)
    finally:
        end_time = strftime("%y%m%d-%H%M%S")
        print('모델생산 종료시간 : ', end_time)
    return total_save_path + '.vec'


def benchmark(filepath, savepath, save_file_name):
    from web import evaluate
    from web.embeddings import load_embedding

    w = load_embedding(filepath, format='word2vec')

    out_fname = os.path.join(savepath) + save_file_name + "_results.csv"

    results = evaluate.evaluate_on_all(w)
    results._ix[1]
    # for ind in results.keys():
    #     print(results._get_axis(0))
    # for ind in results.items():
    #     print(ind)

    # print(results)
    # results.to_csv(out_fname)
    # return results



# benchmark(
#     make_model('/media/leehyunsoo/4TB2/small_data/', 'small_title.txt', '/media/leehyunsoo/4TB2/model/', 'small_title',model = 'skipgram'),
#     '/media/leehyunsoo/4TB2/model/','test')

# FastText Default값
# input,                    : 불러올 데이터
# model = "skipgram",       : 알고리즘 종류 [skipgram, cbow]
# lr = 0.05,                :
# dim = 100,                :
# ws = 5,                   :
# epoch = 5,                : 데이터 처음부터 끝까지 반복하는 횟수
# minCount = 5,             :
# minn = 3,                 : 최소 n gram
# maxn = 6,                 : 최대 n gram
# neg = 5,                  :
# wordNgrams = 1,           :
# loss = "ns",              : [ns, hs, softmax] ns만 사용
# bucket = 2000000,         :
# thread = 12,              : 훈련시 사용할 thread개수
# lrUpdateRate = 100,       :
# t = 1e-4,                 :
