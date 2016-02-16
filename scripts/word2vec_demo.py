import pandas
import random
from gensim.models import word2vec
import numpy as np
import os
import cPickle

BENCHMARK_FILE = 'data/Wylie_tenses.txt'
df = pandas.read_table(BENCHMARK_FILE)['<Wyl_Present>']

models={}
for root,_,files in os.walk('data/output'):
    for f in files:
        if f == 'vocab.txt':
            continue
        loc = os.path.join(root,f)
        models[loc] = word2vec.Word2Vec.load_word2vec_format \
            (loc, binary=True)
    
def print_nn_wordlist(word):
    print(word + '\n----------------------------------')
    for loc,model in models.iteritems():
        print(loc)
        o = model.most_similar(word)
        for res in o[:5]:
            print(res)
        print('----------------------------------')

if __name__ == '__main__':
    ind = np.random.randint(0,len(df), size=10)
    for o in df[ind]:
        try:
            print_nn_wordlist(o.upper())
        except:
            continue
