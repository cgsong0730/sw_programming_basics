import datetime

def print_receipt(lotto_list):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S") # 원하는 형태의 문자열로 변환
    
    print("\n==========================")
    print("      로또 영수증      ")
    print(f"발행일시: {formatted_time}")
    print("--------------------------")
    
    for index, game in enumerate(lotto_list, 1):
        print(f"{index}게임: {game}")
        
    print("==========================")
    print("행운을 빕니다!\n")