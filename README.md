# tibetan_word2vec

###PREREQUISITES
```gensim (sudo pip install gensim)```

###USAGE
put your word2vec binary vectors file in data/output and update it's path in tools/similarity.py
then, to use the similarity metric do:
```from tools.similarity import similarity```
and ```similarity(a,b)``` to get the cosine similarity between words a and b.

NOTE: throws ValueError if a or b aren't in the word list
