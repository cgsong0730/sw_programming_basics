list1 = [23, 3, 45, 26, 76]
maxNum = 1
minNum = 100
for i in list1:
    if i > maxNum:
        maxNum = i
    if i < minNum:
        minNum = i
print(f"최대값: {maxNum}")
print(f"최소값: {minNum}")