import os

corpus = set()
for root,_,files in os.walk('data/clean'):
    for textfile in files:
        with open(os.path.join(root,textfile)) as f:
            corpus |= set(f.read().split())

print('number of syllables: ' + str(len(corpus)))

# print some syllables
#count = 0
#for w in corpus:
#    if count < 300:
#        print(w)
#        count += 1
