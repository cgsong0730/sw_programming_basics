import re

def clean_text(text):
    text = text.lower()                              # 소문자 통일
    text = re.sub(r'<[^>]+>', ' ', text)             # HTML 태그 제거
    text = re.sub(r'http\S+|www\.\S+', ' ', text)    # URL 제거
    text = re.sub(r'[^a-z\s]', ' ', text)            # 영문/공백 외 나머지 문자 제거(숫자·특수문자)
    text = re.sub(r'\s+', ' ', text).strip()         # 중복 공백 정리
    return text

raw = "Hello!!! The price is $100... <br> Visit WWW.example.com NOW."

print(clean_text(raw)) # hello the price is visit now
