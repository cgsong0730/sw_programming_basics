x = 10   # 전역변수
def my_func():
    y = 20   # 지역변수
    print(f"x = {x}, y = {y}")
my_func()   # 결과: x = 10, y = 20
print(y)   # NameError: y는 함수 밖에서 접근 불가

def change_global():
    global x   # 전역변수
    x = 99

change_global()
print(x) # 결과: 99