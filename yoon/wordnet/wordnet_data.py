from nltk.corpus import wordnet

def wordnet_text_training():
    for i in wordnet.all_synsets:
        wordnet_data_result(i)


def wordnet_data_result(synsets):
    return ['physical_entity.n.01', 'hypernyms','entity.n.01', 0.1 ]
