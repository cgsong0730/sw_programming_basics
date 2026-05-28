# 단어장 저장
words = {"apple": "사과", "banana": "바나나", "cherry": "체리"}
with open("words.txt", "w", encoding="utf-8") as f:
    for eng, kor in words.items():
        f.write(f"{eng}:{kor}\n")

# 단어장 불러오기
loaded = {}
with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        eng, kor = line.strip().split(":")
        loaded[eng] = kor
print(loaded["apple"])