PREMIERE_SHOW = 12.0
NORMAL_SHOW = 7.50
DISCOUNT_SHOW = 5.0

full_hall_places = 0.0
incoms_full_hall = 0.0

type_show = input()
num_rows = int(input())
num_cоlumns = int(input())

seats_full_hall = num_rows * num_cоlumns

if type_show == "Premiere":
    incoms_full_hall = PREMIERE_SHOW * seats_full_hall

elif type_show == "Normal":
    incoms_full_hall = NORMAL_SHOW * seats_full_hall
else:
    incoms_full_hall = DISCOUNT_SHOW * seats_full_hall

print(f"{incoms_full_hall:.2f} leva")
