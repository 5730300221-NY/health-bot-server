# encoding: utf-8
import deepcut

def cutThai(text):
    list_word = deepcut.tokenize(text)
    out = u' '.join(list_word).encode('utf-8').strip()
    return out

