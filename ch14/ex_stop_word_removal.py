from nltk.corpus import stopwords
import nltk

# nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

words = ['natural', 'language', 'processing', 'is', 'fun', 'let', 'learn', 'it', 'together']

filtered = [w for w in words if w not in stop_words]
print(filtered) # ['natural', 'language', 'processing', 'fun', 'let', 'learn', 'together']

custom_stops = stop_words.union({'let'}) # 사용자 정의 불용어 추가
filtered2 = [w for w in words if w not in custom_stops]
