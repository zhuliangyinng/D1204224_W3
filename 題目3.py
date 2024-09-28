a = int(input("輸入數字："))
result = {0:"偶數", 1:"奇數"}
print(f"結果：{a} 是{result[a % 2]}")