import random

print("1 から 100 までの数字を当ててください。")
target = random.randint(1,100)
count = 0

while True:
    guess = int(input("入力してください: "))
    count += 1
    if guess < target:
        print("もっと大きい数字です")
    elif guess > target:
        print("もっと小さい数です")
    else:
        print("正解！ " + str(count) + " 回目で当たりました。")
        break
    
