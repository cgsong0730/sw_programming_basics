# 메모 입력받아 파일에 추가
memo = input("메모를 입력하세요: ")
with open("memo.txt", "a", encoding="utf-8") as f:
    f.write(memo + "\n")
print("메모가 저장되었습니다.")

# 저장된 모든 메모 출력
print("--- 저장된 메모 ---")
with open("memo.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")