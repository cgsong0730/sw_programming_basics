from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ['studies', 'running', 'better', 'happily']

stemmed = [stemmer.stem(w) for w in words] # 어간 추출
print(stemmed)
# ['studi', 'run', 'better', 'happili']

lemmas = [lemmatizer.lemmatize(w) for w in words] # 표제어 추출 (품사 지정 시 더 정확)
print(lemmas)
# ['study', 'running', 'better', 'happily']

# 품사(pos)를 알려주면 정확도 상승: v=동사, a=형용사
print(lemmatizer.lemmatize('running', pos='v'))  # run
print(lemmatizer.lemmatize('better', pos='a'))   # good
