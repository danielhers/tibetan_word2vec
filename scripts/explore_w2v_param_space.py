import os
from subprocess import call

# run from root dir

# ignore words repeated under threshold amount of times (0 = don't ignore any words)
vocabulary_thresholds=[0,5]
# word2vec prediction windows around each word
windows = [7,9,5]
# output vector dimension
size = [300, 150]
# number of iterations
iter = [1, 15]

for it in iter:
	for sz in size:
		for win in windows:
			for voc_th in vocabulary_thresholds:
				os.makedirs('data/output/vocab_{vocab_thres}'.format(vocab_thres=vocab_thres), exist_ok=True)
				cmd = "./word2vec/word2vec -train data/corpus.txt -output data/output/vocab_{vocab_thres}/vectors_window_{window}_size_{size}_iter_{iter}.bin -cbow 0 -size {size} -window {window} -negative 25 -hs 0 -sample 1e-4 -threads 12 -binary 1 -iter {iter} -save-vocab data/output/vocab_{vocab_thres}/vocab.txt -min-count {vocab_thres}".format(vocab_thres=, window=, size=, iter=)
				retval = call(cmd.split())
				if retval != 0:
					print('An error has occured. Quitting.')
					break


#os.makedirs('data/output/vocab_{vocab_thres}'.format(vocab_thres=vocab_thres), exist_ok=True)
#cmd = "./word2vec/word2vec -train data/corpus.txt -output data/output/vocab_{vocab_thres}/vectors_window_{window}_size_{size}_iter_{iter}.bin -cbow 0 -size {size} -window {window} -negative 25 -hs 0 -sample 1e-4 -threads 12 -binary 1 -iter {iter} -save-vocab data/output/vocab_{vocab_thres}/vocab.txt -min-count {vocab_thres}".format(vocab_thres=, window=, size=, iter=)
#retval = call(cmd.split())
#if retval != 0:
#	print('An error has occured.')
