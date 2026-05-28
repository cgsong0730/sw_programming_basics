num = 0
for i in range(1, 101):
    for j in range(1, i+1):
        if i % j == 0:
            num += 1
    if num == 2:
        print(f"{i}는 소수이다.")
    num = 0