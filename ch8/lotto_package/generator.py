import random

def generate_numbers(count=1):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    
    return numbers

if __name__ == "__main__":
    print("[테스트 모드] 번호 생성 모듈이 정상 작동합니다.")
    print("생성된 번호:", generate_numbers(1))