# 7번 문제
dice = list(map(int, input().split()))
price = 0

if dice[0] == dice[1]:
    if dice[0] == dice[2]:
        price = 10000 + dice[0] * 1000
    else:
        price = 1000 + dice[0] * 100
elif dice[0] == dice[2]:
    price = 1000 + dice[0] * 100
elif dice[1] == dice[2]:
    price = 1000 + dice[1] * 100
else:
    price = max(dice) * 100

print(price)