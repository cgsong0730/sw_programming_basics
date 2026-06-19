from gensim import corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess

from konlpy.tag import Okt

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# from collections import Counter


# import pyLDAvis
# import pyLDAvis.gensim_models as gensimvis


documents = [
    "주식 시장이 금리 인상 소식에 하락했습니다.",
    "중앙은행은 내년에도 금리를 올릴 가능성이 높다고 발표했습니다.",
    "축구 국가대표팀이 월드컵 예선에서 대승을 거두었습니다.",
    "이번 경기에서 공격수의 득점력이 돋보였습니다.",
    "경제 지표가 악화되면서 투자자들의 불안이 커지고 있습니다.",
    "리그 우승을 향한 선수들의 열정이 대단합니다."
]

okt = Okt()

# 토큰화
tokenized_docs = [okt.nouns(doc) for doc in documents]

# 단어 사전 및 코퍼스(Corpus) 생성
dictionary = corpora.Dictionary(tokenized_docs)
corpus = [dictionary.doc2bow(text) for text in tokenized_docs]

# LDA 모델 학습 - num_topics: 찾고 싶은 주제의 개수, passes: 학습 횟수
lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=15)

# 결과 출력 - 각 토픽을 구성하는 주요 단어 확인
print("### 학습된 토픽 결과 ###")
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic #{idx}: {topic}")

# 새로운 문서가 어떤 토픽에 해당할지 예측
new_doc = "금리가 오르면 주식 가격은 어떻게 될까?"
new_bow = dictionary.doc2bow(okt.nouns(new_doc))
topic_dist = lda_model.get_document_topics(new_bow)
print(f"\n새 문서의 토픽 분포: {topic_dist}")


