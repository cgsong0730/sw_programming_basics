# 기본값 매개변수
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님!")

greet("홍길동")                    # 출력: 안녕하세요, 홍길동님!
greet("이순신", "반갑습니다")      # 출력: 반갑습니다, 이순신님!

# 키워드 인자
def info(name, age, city):
    print(f"{name}, {age}세, {city}")

info(city="서울", name="강감찬", age=25)