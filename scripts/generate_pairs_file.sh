#!/usr/bin/env bash

(cut -f1 -d' ' word2vec/vocab_5/vocab.txt; echo EXIT) |
~/tibetan/tibetan_word2vec/word2vec/distance word2vec/vocab_5/vectors_window_10_size_152_iter_5.bin |
grep -v '^Enter word\|^-*$\|^\s*Word\s*Cosine distance$' |
sed 's/^Word:\s*//; s/\s*Position in vocabulary:.*//' > word2vec/vocab_5/pairs.txt