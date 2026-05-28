anser1 = input("주말에 보통 밖에 있나요 집에 있나요? y or n") # y - e, n - i
anser2 = input("자기 전 침대에서 상상을 즐기나요? y or n") # y - n, n - s
anser3 = input("친구가 어려운 상황에 처했을 때, 위로해주나요(y) 아니면 솔루션을 제시하나요(n)? y or n")
anser4= input("아침에 날씨를 자주 확인하나요? y or n")  # y - j, n - p

if anser1 == "y":
    if anser2 == "y":
        if anser3 == "y":
            if anser4 == "y":
                print("당신은 ENFJ입니다.")
            else:
                print("당신은 ENFP입니다.")
        else:
            if anser4 == "y":
                print("당신은 ENTJ입니다.")
            else:
                print("당신은 ENTP입니다.")
    else:
        if anser3 == "y":
            if anser4 == "y":
                print("당신은 ESFJ입니다.")
            else:
                print("당신은 ESFP입니다.")
        else:
            if anser4 == "y":
                print("당신은 ESTJ입니다.")
            else:
                print("당신은 ESTP입니다.")
else:
    if anser2 == "y":
        if anser3 == "y":
            if anser4 == "y":
                print("당신은 INFJ입니다.")
            else:
                print("당신은 INFP입니다.")
        else:
            if anser4 == "y":
                print("당신은 INTJ입니다.")
            else:
                print("당신은 INTP입니다.")
    else:
        if anser3 == "y":
            if anser4 == "y":
                print("당신은 ISFJ입니다.")
            else:
                print("당신은 ISFP입니다.")
        else:
            if anser4 == "y":
                print("당신은 ISTJ입니다.")
            else:
                print("당신은 ISTP입니다.")