type_flowers = input()
num_flowers = int(input())
budget = int(input())

sum_pay = 0
left_sum = 0

PRICE_ROSE = 5
PRICE_DAHLIA = 3.8
PRICE_TULIP = 2.80
PRICE_NARCISSUS = 3
PRICE_GLADIOLUS = 2.5

PERCENT_ROSES = 0.10
PERCENT_DAHLIAS = 0.15
PERCENT_TULIPS = 0.15
PERCENT_NARCISSUS = 0.15
PERCENT_GLADIOLUS = 0.20

if type_flowers == "Roses":
    if num_flowers > 80:
        sum_pay = num_flowers * PRICE_ROSE
        sum_pay = sum_pay - sum_pay * PERCENT_ROSES
    else:
        sum_pay = num_flowers * PRICE_ROSE
elif type_flowers == "Dahlias":
    if num_flowers > 90:
        sum_pay = num_flowers * PRICE_DAHLIA
        sum_pay = sum_pay - sum_pay * PERCENT_DAHLIAS
    else:
        sum_pay = num_flowers * PRICE_DAHLIA
elif type_flowers == "Tulips":
    if num_flowers > 80:
        sum_pay = num_flowers * PRICE_TULIP
        sum_pay = sum_pay - sum_pay * PERCENT_TULIPS
    else:
        sum_pay = num_flowers * PRICE_TULIP
elif type_flowers == "Narcissus":
    if num_flowers < 120:
        sum_pay = num_flowers * PRICE_NARCISSUS
        sum_pay = sum_pay + sum_pay * PERCENT_NARCISSUS
    else:
        sum_pay = num_flowers * PRICE_NARCISSUS
elif type_flowers == "Gladiolus":
    if num_flowers < 80:
        sum_pay = num_flowers * PRICE_GLADIOLUS
        sum_pay = sum_pay + sum_pay * PERCENT_GLADIOLUS
    else:
        sum_pay = num_flowers * PRICE_GLADIOLUS

left_sum = abs(sum_pay - budget)

if sum_pay <= budget:
    print(f"Hey, you have a great garden with {num_flowers} {type_flowers} and {left_sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_sum:.2f} leva more.")
