month_rent = input()
num_spent_night = int(input())

discount_studio = 0
discount_apartment = 0
price_studio = 0
price_apartment = 0.0
price_spent_time_studio = 0
price_spent_time_apartment = 0
total_price_apartment = 0.0
total_price_studio = 0.0

if month_rent == "May" or month_rent == "October":
    price_studio = 50
    price_apartment = 65
    if num_spent_night > 14:
        discount_studio = 0.30
        discount_apartment = 0.10
    elif num_spent_night > 7:
        discount_studio = 0.05
elif month_rent == "June" or month_rent == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if num_spent_night > 14:
        discount_studio = 0.20
        discount_apartment = 0.10
elif month_rent == "July" or month_rent == "August":
    price_studio = 76
    price_apartment = 77
    if num_spent_night > 14:
        discount_apartment = 0.10

total_price_apartment = price_apartment - price_apartment * discount_apartment
price_spent_time_apartment = total_price_apartment * num_spent_night

total_price_studio = price_studio - price_studio * discount_studio
price_spent_time_studio = total_price_studio * num_spent_night

print(f"Apartment: {price_spent_time_apartment:.2f} lv.")
print(f"Studio: {price_spent_time_studio:.2f} lv.")
