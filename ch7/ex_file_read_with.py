with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("with 문은 안전하다.\n")

with open("diary.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())