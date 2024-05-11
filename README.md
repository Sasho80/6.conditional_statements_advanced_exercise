01.Problem: . Cinema
In a movie theater, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of screenings with tickets at different prices:
• Premiere - premiere screening, at a price of BGN 12.00;
• Normal - standard projection, at a price of BGN 7.50;
• Discount - screening for children, schoolchildren and students at a reduced price of BGN 5.00.
Write a program that reads the projection type (text), number of rows and number of columns in the hall (integers) entered by the user and calculates the total ticket revenue for a full house. Print the result in 2 decimal places format.
Sample input output
input	    output		input	  output		input	   output
Premiere  1440.00 	        Normal  2047.50                 Discount   1800.00
10        leva                  21      leva                    12         leva
12	 	                13                              30

02.Problem: Summer outfit
Summer is a season with very changeable weather and Victor needs your help. Write a program that, based on the time of day and the degrees, recommends Victor what clothes to wear. Your friend has different plans for each stage of the day, which also require a different appearance - you can see them from the table.
Exactly two lines are read from the console:
• Degrees - whole number;
• Time of day - text with three options "Morning", "Afternoon" or "Evening".

Time of day / degrees          Morning            Afternoon	             Evening
10 <= degrees <= 18	     Outfit = Sweatshirt     Outfit = Shirt          Outfit = Shirt
                          Shoes = Sneakers	    Shoes = Moccasins        Shoes = Moccasins
                          
18 < degrees <= 24	      Outfit = Shirt        Outfit = T-Shirt          Outfit = Shirt
                        Shoes = Moccasins	       Shoes = Sandals          Shoes = Moccasins
                        
degrees >= 25         	Outfit = T-Shirt        Outfit = Swim Suit         Outfit = Shirt
                         Shoes = Sandals	       Shoes = Barefoot          Shoes = Moccasins

As output, print to the console one line: "It's {degrees} degrees, get your {clothes} and {shoes}."

Sample input output
input	          output
16              It's 16 degrees, get your
Morning	        Sweatshirt and Sneakers.

input	          output
22              It's 22 degrees, get your 
Afternoon	      T-Shirt and Sandals.

input	          output
28              It's 28 degrees, get your
Evening	        Shirt and Moccasins.

03.Problem: New house
Marin and Nellie buy a house not far from Sofia. Nellie loves flowers so much that she convinces you to write a
program to calculate how much it will cost them to plant a certain number of flowers and whether the available 
budget will be enough for them. Different flowers have different prices:

flower                 Rose        Dahlia         Tulip       Narcissus     Gladiola
Price per piece in     5	   3.80	          2.80	      3	            2.50
leva

The following discounts are available:
• If Nellie buys more than 80 Roses - 10% discount from the final price;
• If Nellie buys more than 90 Dahlias - 15% discount from the final price;
• If Nellie buys more than 80 Tulips - 15% discount from the final price;
• If Nellie buys less than 120 Narcissus - the price increases by 15%;
• If Nellie Buys less than 80 Gladioli - the price increases by 20%.
3 lines are read from the console:
• Flower type - text with options "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus";
• Number of flowers - integer;
• Budget - integer.
To print to the console on one line:
• If their budget is sufficient - "Hey, you have a great garden with {number of flowers} {type of flowers} and {remaining amount} leva left.";
• If their budget is NOT enough - "Not enough money, you need {necessary amount} leva more.".
Amount to be formatted to the second decimal place.

Sample input and output
input   output
Roses   Not enough money, 
55      you need 25.00 leva more.
250	

input   output
Tulips  Hey, you have a great  garden with
88      88 Tulips and 50.56 leva left.
260	

input      output
Narcissus  Not enough money, you need 
119        50.55 leva more.
360

04.Problem: Fishing boat
Tony and friends love to go fishing and are so passionate about fishing that they decide to go fishing by boat. The price for renting the vessel 
depends on the season and the number of fishermen:
Depending on the season:
• The price for renting the ship in the spring is BGN 3,000;
• The price for renting the ship in summer and autumn is BGN 4,200;
• The price for renting the ship in winter is BGN 2,600.
Depending on the number of the group, there is a different discount:
• If the group is up to 6 people inclusive - 10% discount;
• If the group is from 7 to 11 people inclusive - 15% discount;
• If the group is 12 or more - 25% discount.
Fishermen enjoy an additional 5% discount if they are an even number, unless it is autumn - then they do not have an additional discount, which is 
charged after deducting the discount according to the above criteria.
Write a program to calculate whether the fishermen will collect enough money.
input
Three lines are read from the console:
• Group budget - whole number;
• Season - text: "Spring", "Summer", "Autumn" or "Winter";
• Number of fishermen - integer.
output
The following should be printed on the console:
• If the budget is sufficient:
"Yes! You have {the remaining money} leva left."
• If the budget IS NOT sufficient:
"Not enough money! You need {amount that does not reach} leva."
Amounts must be formatted to two decimal places.

Sample input and output
input   output
3000    Not enough money! 
Summer  You need 570.00 leva.
11	

input    output
3600     Not enough money! 
Autumn   You need 180.00 leva.
6	

input    output
2000     Yes! You have 
Winter   50.00 leva left.
13

05.Problem: Journey
A young programmer has a certain budget and free time in a given season. Write a program that accepts as input the budget and the season, and outputs where the programmer will rest and how much he will spend.
The budget determines the destination, and the season determines how much of the budget will be spent. If it is summer, he will rest at a campsite, and in winter at a hotel. If he is in Europe, regardless of the season, he will rest in a hotel. Each campsite or hotel, according to the destination, has its own price, which corresponds to a certain percentage of the budget:
• At BGN 100 or less - somewhere in Bulgaria:
o Summer - 30% of the budget;
o Winter - 70% of the budget.
• At BGN 1000 or less - somewhere in the Balkans:
o Summer - 40% of the budget;
o Winter - 80% of the budget.
• For more than BGN 1,000 - somewhere in Europe:
o When traveling in Europe, regardless of the season, will spend 90% of the budget.
Login
The input is read from the console and consists of two lines entered by the user:
• Budget - real number;
• One of the two possible seasons - "summer" or "winter".
Exit
Two lines should be printed to the console:
• "Somewhere in [destination]" between "Bulgaria", "Balkans" and "Europe"
• "{Type of vacation} - {Amount spent}":
o Rest can be between "Camp" and "Hotel"
o The amount must be formatted to the second decimal place 

input    output
50       Somewhere in Bulgaria
summer	 Camp - 15.00

input    output
75       Somewhere in Bulgaria
winter	 Hotel - 52.50

input    output
312      Somewhere in Balkans
summer	 Camp - 124.80

input    output
678.53   Somewhere in Balkans
winter	 Hotel - 542.82

input    output
1500     Somewhere in Europe
summer	 Hotel - 1350.00

06.Problem: Operations between numbers
Write a program that reads two integers (N1 and N2) and an operator to perform a given mathematical operation. The possible operations are: Addition(+), Subtraction(-), Multiplication(*), Division(/) and Modular Division(%). Addition, subtraction and multiplication on the console should print the result and whether it is even or odd. In ordinary division - the result. In the case of modular division - the remainder. It should be noted that the divisor can be equal to 0 (zero), and is not divisible by zero. In this case, a special message should be printed.
input
3 lines entered by the user are read from the console:
• N1 - integer;
• N2 - integer;
• Operator - one symbol among: "+", "-", "*", "/", "%".
output
To print one line to the console:
• If the operation is addition, subtraction or multiplication:
o "{N1} {operator} {N2} = {result} - {even/odd}"
• If the operation is division:
o "{N1} / {N2} = {result}" - result formatted to the second decimal place
• If the operation is modular division:
o "{N1} % {N2} = {remainder}"
• In case of division by 0 (zero):
o "Cannot divide {N1} by zero"

Sample input and output
input   output
10      10 + 12 = 22 - even
12
+	

input   output
10      10 - 1 = 9 - odd
1
-	

input   output
7       7 * 3 = 21 - odd
3
*	

input   output
123     123 / 12 = 10.25
12
/	

input   output
10      10 % 3 = 1
3
%	

input   output
112     Cannot divide 112 by zero
0
/	

input   output
112     Cannot divide 112 by zero
0
/

07.Problem: Hotel room
Hotel offers 2 types of rooms: studio and apartment. Write a program that calculates the total stay price for a studio and an apartment. 
Prices depend on the month of stay:

May and October            June and September             July and August
Studio - BGN 50/night      Studio - BGN 75.20/night       Studio - BGN 76/night
Apartment - BGN 65/night   Apartment - BGN 68.70/night    Apartment - BGN 77/night

The following discounts are also available:
• For studio, for more than 7 nights in May and October: 5% discount.
• For studio, for more than 14 nights in May and October: 30% discount.
• For studio, for more than 14 nights in June and September: 20% discount.
• For an apartment, for more than 14 nights, regardless of the month: 10% discount.
input
The input is read from the console and contains exactly 2 lines entered by the user:
• On the first line is the month - May, June, July, August, September or October;
• On the second line is the number of overnight stays - an integer.
output
To print 2 lines to the console:
• On the first line: "Apartment: {price for entire stay} lv."
• On the second line: "Studio: {price for entire stay} lv."
The price for the entire stay must be formatted to two decimal places.

Sample  input and output
input   output
May     Apartment: 877.50 lv.
15	Studio: 525.00 lv.

input	output
May     Apartment: 877.50 lv.
15	Studio: 525.00 lv.

08.Problem: On time for the exam
A student must go to an exam at a specific time (for example, 9:30 a.m.). He comes to the exam hall at a given arrival time (eg 9:40). The student is considered to have arrived on time if he arrived at the time of the exam or up to half an hour before. If he arrived more than 30 minutes earlier, he was late. If he came after the exam time, he is late. Write a program that reads an exam time and an arrival time and prints whether the student was on time, whether he was early or late, and how many hours or minutes he was early or late.
input
4 integers (one per line) entered by the user are read from the console:
• The first line contains the time of the exam - an integer from 0 to 23;
• The second line contains the minute of the exam - an integer from 0 to 59;
• The third line contains the arrival time - an integer from 0 to 23;
• The fourth line contains the arrival minute - an integer from 0 to 59.
output
On the first line, print:
• "Late" if the student arrives later than the exam time;
• "On time", if the student arrives exactly at the time of the exam or up to 30 minutes earlier;
• "Early" if the student arrives more than 30 minutes before the exam time.
If the student arrives at least one minute after the exam time, print on the next line:
• "mm minutes before the start" for arriving earlier by less than an hour;
• "hh:mm hours before the start" to advance by 1 hour or more. Always print minutes with 2 digits, for example "1:05";
• "mm minutes after the start" for a delay of less than an hour;
• "hh:mm hours after the start" for a delay of 1 hour or more. Always print minutes with 2 digits, for example "1:03".

Sample input and output
input       output                 
9           Late                        
30          20 minutes after the start
9
50


input       output  
9           On time
00          30 minutes before the start
8
30

input    output
16       Early
00       1:00 hours before the start
15
00

input    output
9        Late
00       1:30 hours after the start
10
30

input   output
14      On time
00      5 minutes before the start
13
55

input  output
11     Early
30     3:18 hours before the start
8
12

input  output
10     On time
00
10
00

input  output
11     Early
30     35 minutes before the start
10
55

input output
11    Late
30    59 minutes after the start
12
29

09. Problem: Ski trip
Atanas decides to spend his vacation in Bansko and go skiing. Before he goes, however, he needs to book a hotel and calculate how much the stay will cost him. The following types of rooms are available, with the following prices for a stay:
 "room for one person" – BGN 18.00 per night
 "apartment" – BGN 25.00 per night
 "president apartment" – BGN 35.00 per night
According to the number of days he will stay in the hotel (example: 11 days = 10 nights) and the type of room he will choose, he can enjoy a different discount.
The reductions are as follows:

type of premises                 less than 10 days              between 10 and 15 days                   more than 15 days
room for one person           does not use a discount           does not use a discount                 does not use a discount    
apartment                      30% of the final price           35% of the final price                  50% of the final price
president apartment           10% of the final price            15% of the final price                  20% of the final price

After the stay, Atanas' assessment of the hotel's services may be positive or negative. If his assessment is positive, Atanas adds 25% of it to the price with the discount already deducted. If his assessment is negative, 10% will be deducted from the price.
input
The input is read from the console and consists of three lines:
• First row - days of stay - an integer in the interval [0...365]
• Second row - room type - "room for one person", "apartment" or "president apartment"
• Third row - evaluation - "positive" or "negative"
output
One line should be printed to the console:
• The price of his hotel stay, formatted to the second decimal place.

Sample    input and output

input	   output
14         264.06
apartment
positive

input       output
30          730.80
president 
apartment
negative	

input       output
12          247.50
room for 
one person
positive

input       output
12          247.50
room for 
one person
positive	

















	











