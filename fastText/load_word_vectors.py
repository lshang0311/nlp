import io
import os

"""
https://fasttext.cc/docs/en/english-vectors.html

"""


def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    print("n = {},  d = {}".format(n, d))

    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])

    return data


# get all
# data = load_vectors('./data/wiki-news-300d-1M.vec')

# get a short vector
# lshang@ubuntu:~/work.github/nlp$ cat wiki-news-300d-1M.vec | head -n 51 > words_short.vec

path = r"./fastText/data"
path = os.path.abspath(path)
file_name = 'words_short.vec'
# file_name = 'wiki-news-300d-1M.vec'
full_file_name = os.path.join(path, file_name)

vector = load_vectors(full_file_name)

print(vector)
