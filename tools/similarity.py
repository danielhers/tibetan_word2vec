from gensim.models import word2vec

MODEL_PATH='data/output/vocab_5/vectors_window_9_size_152_iter_1.bin'
MODEL = word2vec.Word2Vec.load_word2vec_format(MODEL_PATH, binary=True)

print('Loading model...')

def similarity(a,b):
    return MODEL.similarity(a,b)
