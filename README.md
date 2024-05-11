01.Problem: . Cinema
In a movie theater, the chairs are arranged in a rectangular shape in r rows and c columns. There are three types of screenings with tickets at different prices:
• Premiere - premiere screening, at a price of BGN 12.00;
• Normal - standard projection, at a price of BGN 7.50;
• Discount - screening for children, schoolchildren and students at a reduced price of BGN 5.00.
Write a program that reads the projection type (text), number of rows and number of columns in the hall (integers) entered by the user and calculates the total ticket revenue for a full house. Print the result in 2 decimal places format.
Sample input output
input	    output		input	  output		input	   output
Premiere  1440.00 	Normal  2047.50   Discount 1800.00
10        leva      21      leva      12       leva
12	 	              13                30

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
Price per piece in     5	         3.80	          2.80	      3	            2.50
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





