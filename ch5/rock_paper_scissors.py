import random

user_input = input("가위, 바위, 보 중 하나를 입력하세요: ")
options = ["가위", "바위", "보"]
computer_input = random.choice(options)
if user_input == computer_input and user_input in options:
    result = "비겼습니다!"
elif (user_input == "가위" and computer_input == "보") or \
    (user_input == "바위" and computer_input == "가위") or \
    (user_input == "보" and computer_input == "바위"):
    result = "이겼습니다!"
elif (user_input == "가위" and computer_input == "바위") or \
    (user_input == "바위" and computer_input == "보") or \
    (user_input == "보" and computer_input == "가위"):
    result = "졌습니다..."
else:
    result = "에러 발생: '가위', '바위', '보' 중 하나만 입력해야 합니다."

print(f"사용자: {user_input}")
print(f"컴퓨터: {computer_input}")
print(f"게임 결과: {result}")
