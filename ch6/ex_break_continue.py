sensor_data = [25, -5, 32, -10, 105, 28, 30]
print("--- 온도 센서 점검을 시작합니다 ---")
for temp in sensor_data:
    if temp < 0:
        print(f"  [오류] 잘못된 데이터 무시: {temp}도")
        continue  
    if temp > 100:
        print(f"[경고] {temp}도 초과! 화재 위험으로 시스템을 즉시 정지합니다.")
        break     
    print(f"정상 온도 기록: {temp}도")
print("--- 온도 센서 점검이 종료되었습니다 ---")