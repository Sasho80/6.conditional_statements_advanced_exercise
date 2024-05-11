budget = float(input())
season = input()

destination = ""
discount_budget_summer = 0.30
place_journey = " "

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.30
        place_journey = "Camp"
    else:
        budget *= 0.70
        place_journey = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.40
        place_journey = "Camp"
    else:
        budget *= 0.80
        place_journey = "Hotel"
else:
    destination = "Europe"
    budget *= 0.90
    place_journey = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_journey} - {budget:.2f}")
