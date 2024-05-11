budget_group = int(input())
season = input()
num_fisherman = int(input())

price_ship = 0
discount_fisherman = 0
left_money = 0

if season == "Spring":
    price_ship = 3000
elif season == "Summer" or season == "Autumn":
    price_ship = 4200
else:
    price_ship = 2600

if num_fisherman <= 6:
    discount_fisherman = 0.10
    price_ship -= price_ship * discount_fisherman
elif 7 <= num_fisherman <= 11:
    discount_fisherman = 0.15
    price_ship -= price_ship * discount_fisherman
else:
    discount_fisherman = 0.25
    price_ship -= price_ship * discount_fisherman

if (num_fisherman % 2 == 0) and (season == "Winter" or season == "Summer" or season == "Spring"):
    discount_fisherman = 0.05
    price_ship -= price_ship * discount_fisherman

left_money = abs(budget_group - price_ship)

if budget_group >= price_ship:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")
    