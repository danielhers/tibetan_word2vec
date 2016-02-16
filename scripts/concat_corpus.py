import os
import re

corpus = ''
for root,_,files in os.walk('data/clean'):
    for textfile in files:
        with open(os.path.join(root,textfile)) as f:
            corpus += ' '
            corpus += f.read()    

with open('data/corpus.txt','w') as f:
    f.write(corpus)
