import sys

score = int(input("1부터 100 사이의 점수를 입력하세요: "))
if not (1 <= score <= 100):
    sys.stderr.write("에러: 점수는 1에서 100 사이의 값이어야 합니다.\n")
    sys.exit(1)
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f"입력하신 점수는 {score}점이며, 성적은 '{grade}'입니다.")