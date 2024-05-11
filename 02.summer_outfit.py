degree = int(input())
time_day = input()

OUTFIT = ""
SHOES = ""

if 10 <= degree <= 18:
    if time_day == "Morning":
        OUTFIT = "Sweatshirt"
        SHOES = "Sneakers"
    elif time_day == "Afternoon":
        OUTFIT = "Shirt"
        SHOES = "Moccasins"
    elif "Evening" == time_day:
        OUTFIT = "Shirt"
        SHOES = "Moccasins"

elif 18 < degree <= 24:
    if time_day == "Morning":
        OUTFIT = "Shirt"
        SHOES = "Moccasins"
    elif time_day == "Afternoon":
        OUTFIT = "T-Shirt"
        SHOES = "Sandals"
    elif "Evening" == time_day:
        OUTFIT = "Shirt"
        SHOES = "Moccasins"
elif degree >= 25:
    if time_day == "Morning":
        OUTFIT = "T-Shirt"
        SHOES = "Sandals"
    elif time_day == "Afternoon":
        OUTFIT = "Swim Suit"
        SHOES = "Barefoot"
    elif "Evening" == time_day:
        OUTFIT = "Shirt"
        SHOES = "Moccasins"

print(f"It's {degree} degrees, get your {OUTFIT} and {SHOES}.")
