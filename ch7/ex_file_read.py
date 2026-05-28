# 방법 1: read() - 전체 한꺼번에 읽기
f = open("diary.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# 방법 2: for 문 - 한 줄씩 처리
f = open(" diary.txt", "r", encoding="utf-8")
content = f.readlines()
for line in content:
    print(line.strip())    # strip()으로 \n 제거
f.close()