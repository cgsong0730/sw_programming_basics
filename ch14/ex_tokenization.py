import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download('punkt')          # 예전 NLTK 버전 – 최초 1회 실행
# nltk.download('punkt_tab')      # 최신 NLTK 버전 – 최초 1회 실행
text = "Natural language processing is fun. Let's learn it together."

words = word_tokenize(text)     # 단어 토큰화
print(words)
# ['Natural', 'language', 'processing', 'is', 'fun', '.', 'Let', "'s", 'learn', 'it', 'together', '.']

sentences = sent_tokenize(text) # 문장 토큰화
print(sentences)
# ['Natural language processing is fun.', "Let's learn it together."]
