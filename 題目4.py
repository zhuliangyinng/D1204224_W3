a = int(input("請輸入一個三位數："))
total = sum(int(digit) for digit in str(a))
print(f"每位數字的總和：{total}")