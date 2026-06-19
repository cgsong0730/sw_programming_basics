from collections import Counter
import re

docs = [
    "I love machine learning",
    "I love deep learning",
    "deep learning is fun"
]

# 1) 토큰화
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

tokenized = [tokenize(d) for d in docs]

# 2) 어휘 사전(vocabulary) 만들기
vocab = sorted(set(word for doc in tokenized for word in doc))
print("어휘 사전:", vocab)

# 3) 각 문서를 카운트 벡터로 변환
def to_bow(tokens, vocab):
    counts = Counter(tokens)
    return [counts[word] for word in vocab]

for doc, tokens in zip(docs, tokenized):
    print(f"{doc!r:35} -> {to_bow(tokens, vocab)}")