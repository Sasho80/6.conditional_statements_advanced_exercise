days_stay = int(input())
type_room = input()
evaluation = input()
оvernight_stays = days_stay - 1

price_overnight_stay = 0
discount_overnight_stays = 0
total_price_overnight_stays = 0

PRICE_APARTMENT = 25.00
PRICE_PRESIDENT_APARTMENT = 35.00
PRICE_ROOM_PERSON = 18.00

if type_room == "room for one person":
    price_overnight_stay = оvernight_stays * PRICE_ROOM_PERSON

elif days_stay < 10 and type_room == "apartment":
    discount_apartment = 0.30
    price_overnight_stay = оvernight_stays * PRICE_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_apartment

elif days_stay < 10 and type_room == "president apartment":
    discount_president_apartment = 0.10
    price_overnight_stay = оvernight_stays * PRICE_PRESIDENT_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_president_apartment

elif 15 > days_stay > 10 and type_room == "apartment":
    discount_apartment = 0.35
    price_overnight_stay = оvernight_stays * PRICE_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_apartment

elif 15 > days_stay > 10 and type_room == "president apartment":
    discount_apartment = 0.15
    price_overnight_stay = оvernight_stays * PRICE_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_apartment

elif days_stay > 15 and type_room == "apartment":
    discount_apartment = 0.50
    price_overnight_stay = оvernight_stays * PRICE_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_apartment

elif days_stay > 15 and type_room == "president apartment":
    discount_president_apartment = 0.20
    price_overnight_stay = оvernight_stays * PRICE_PRESIDENT_APARTMENT
    discount_overnight_stays = price_overnight_stay - price_overnight_stay * discount_president_apartment

if discount_overnight_stays != 0:
    price_overnight_stay = discount_overnight_stays

if evaluation == "positive":
    discount_positive = 0.25
    total_price_overnight_stays = price_overnight_stay + price_overnight_stay * discount_positive
elif evaluation == "negative":
    discount_negative = 0.10
    total_price_overnight_stays = price_overnight_stay - price_overnight_stay * discount_negative

print(f"{total_price_overnight_stays:.2f}")
