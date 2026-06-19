import math
from collections import Counter
import re

docs = [
    "I love machine learning",
    "I love deep learning",
    "deep learning is fun"
]

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

tokenized = [tokenize(d) for d in docs]
vocab = sorted(set(word for doc in tokenized for word in doc))
N = len(docs)

# 1) TF: 문서 내 단어 빈도 (전체 단어 수로 나눠 정규화)
def compute_tf(tokens):
    counts = Counter(tokens)
    total = len(tokens)
    return {word: counts[word] / total for word in counts}

# 2) IDF: log(전체 문서 수 / 그 단어가 등장한 문서 수)
def compute_idf(tokenized, vocab):
    idf = {}
    for word in vocab:
        df = sum(1 for doc in tokenized if word in doc)  # 등장 문서 수
        idf[word] = math.log(N / df)
    return idf

idf = compute_idf(tokenized, vocab)

# 3) TF-IDF = TF * IDF
for doc, tokens in zip(docs, tokenized):
    tf = compute_tf(tokens)
    vec = [round(tf.get(w, 0) * idf[w], 3) for w in vocab]
    print(f"{doc!r:30} -> {vec}")

print("\n어휘:", vocab)