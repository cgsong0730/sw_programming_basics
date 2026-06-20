vocab = ['deep', 'fun', 'is', 'learning', 'love', 'machine']
tfidf_matrix = [
    [0.0,   0.0,   0.0,   0.0,   0.101, 0.275],  # 'I love machine learning'
    [0.101, 0.0,   0.0,   0.0,   0.101, 0.0],    # 'I love deep learning'
    [0.101, 0.275, 0.275, 0.0,   0.0,   0.0],    # 'deep learning is fun'
]
docs = ['I love machine learning', 'I love deep learning', 'deep learning is fun']

# 1) 각 단어에 감성 점수(polarity) 부여: 긍정 +, 부정 -, 중립 0
polarity = {
    'love':     1.0,   # 긍정
    'fun':      1.0,   # 긍정
    'deep':     0.0,   # 중립
    'is':       0.0,   # 중립
    'learning': 0.0,   # 중립
    'machine':  0.0,   # 중립
}
weights = [polarity[w] for w in vocab]

# 2) 문서 감성 점수 = TF-IDF 벡터 · 감성 가중치 (내적)
def sentiment_score(vec):
    return sum(v * w for v, w in zip(vec, weights))

def to_label(score):
    if score > 0:
        return '긍정'
    if score < 0:
        return '부정'
    return '중립'

print("=== [방식 1] 사전 기반 감성 분석 ===")
for doc, vec in zip(docs, tfidf_matrix):
    s = sentiment_score(vec)
    print(f"{doc:30} 점수={s:+.3f}  ->  {to_label(s)}")


# ------------------------------------------------------------
# [방식 2] 지도학습(supervised) - 분류기를 학습시키는 실무 방식
# 실제 감성 분석은 정답 라벨이 달린 데이터로 모델을 학습합니다.
# 주어진 3문장은 모두 긍정이라, 학습을 위해 부정 예시를 추가했습니다.
# ------------------------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train_texts = [
    'I love machine learning',      # 긍정
    'I love deep learning',         # 긍정
    'deep learning is fun',         # 긍정
    'I hate this boring lecture',   # 부정
    'this is terrible and sad',     # 부정
    'machine learning is awful',    # 부정
]
train_labels = [1, 1, 1, 0, 0, 0]   # 1 = 긍정, 0 = 부정

# 텍스트를 TF-IDF 벡터로 변환
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(train_texts)

# 로지스틱 회귀 분류기 학습
clf = LogisticRegression()
clf.fit(X, train_labels)

# 새로운 문장에 대해 예측
test_texts = [
    'I love deep learning',
    'this lecture is awful and boring',
]
X_test = vectorizer.transform(test_texts)
preds = clf.predict(X_test)
probs = clf.predict_proba(X_test)[:, 1]   # 긍정일 확률

print("\n=== [방식 2] 지도학습 기반 감성 분석 ===")
for text, p, prob in zip(test_texts, preds, probs):
    label = '긍정' if p == 1 else '부정'
    print(f"{text:35} ->  {label} (긍정 확률 {prob:.2f})")