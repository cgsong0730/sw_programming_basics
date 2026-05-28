command = "quit"
match command:
    case "start":
        print("프로그램을 시작합니다.")
    case "quit":
        print("프로그램을 종료합니다.") # 실행됨
    case _:
        print("알 수 없는 명령입니다.")