from lotto_package import generator, printer

def start_machine():
    print("=== 행운의 로또 자판기 ===")

    games_count = int(input("몇 게임을 구매하시겠습니까? (숫자 입력): "))

    lotto_list = []
    
    for _ in range(games_count):
        numbers = generator.generate_numbers()
        lotto_list.append(numbers)
        
    printer.print_receipt(lotto_list)

if __name__ == "__main__":
    start_machine()