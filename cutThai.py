# encoding: utf-8
import deepcut

def cutThai(list_word):
    a = deepcut.tokenize(list_word)
    out = u' '.join(list_word).encode('utf-8').strip()
    return out
