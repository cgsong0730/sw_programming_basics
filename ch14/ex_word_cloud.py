from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 어휘 사전과 문서별 TF-IDF 벡터
vocab = ['deep', 'fun', 'is', 'learning', 'love', 'machine']
tfidf_matrix = [
    [0.0,   0.0,   0.0,   0.0,   0.101, 0.275],  # 'I love machine learning'
    [0.101, 0.0,   0.0,   0.0,   0.101, 0.0],    # 'I love deep learning'
    [0.101, 0.275, 0.275, 0.0,   0.0,   0.0],    # 'deep learning is fun'
]

# 단어별 TF-IDF 점수를 전체 문서에 대해 합산해 가중치 사전 만들기
word_weights = {}
for col, word in enumerate(vocab):
    total = sum(row[col] for row in tfidf_matrix)
    if total > 0:                      # 가중치가 0인 단어(예: learning)는 제외
        word_weights[word] = total

print("단어별 가중치:", word_weights)

# 워드 클라우드 생성 (글자 크기는 가중치에 비례)
wc = WordCloud(
    width=800,
    height=400,
    background_color='white',
    colormap='viridis',
    prefer_horizontal=0.9,
    relative_scaling=0.5,
).generate_from_frequencies(word_weights)

# 파일로 저장
wc.to_file('tfidf_wordcloud.png')

# 화면에 표시
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()