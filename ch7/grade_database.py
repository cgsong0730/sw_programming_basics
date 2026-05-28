scores = {"홍길동": 85, "이순신": 92, "강감찬": 78, "세종대왕": 95}

# 모든 학생의 점수 출력 (items() 활용)
for name, score in scores.items():
    print(f"{name}: {score}점")

# 평균 점수 계산
avg = sum(scores.values()) / len(scores)
print(f"평균 점수: {avg:.1f}점")
# 출력: 평균 점수: 87.5점