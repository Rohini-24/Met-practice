#1. Any customer will order two dishes
#2. ANy customer will enter quantity for each dish
#3. Calculate the total bill for the user.


#1. what you want to acheive?
   ## Total Bill
#2. What do u need to acheive that?
   # Dishes and their prices
   # What user wants 
   # how many the user wants
#3. Arrange the order
   # Dishes and their prices - Done
   # What user wants - DOne
   # how many the user wants
   #Total Bill

#4. write the code

total_bill = 0
menu = {
    "dosa": 40,
    "idly": 35,
    "poori": 45,
    "wada": 50,
    "upma": 30
}

dish_one_choice = input("What do you want?") #idly
dish_one_quantity = int(input("How many?")) #20

dish_two_choice = input("What do you want?")
dish_two_quantity = int(input("How many?"))

dish_one_bill = (dish_one_quantity * menu.get(dish_one_choice))
dish_two_bill = (dish_two_quantity * menu.get(dish_two_choice))

total_bill =  dish_one_bill + dish_two_bill

detailed_bill = f"""

#####WELCOME TO SO AND SO HOTEL######
BILL ID: {total_bill * 32}

{dish_one_choice} X {menu.get(dish_one_choice)} = {dish_one_bill}
{dish_two_choice} X {menu.get(dish_two_choice)} = {dish_two_bill}
-------------------------------------------------------------------
GST: 0%
TAXES: 0%
------------------------------------TOTAL BILL: Rs.{total_bill}/----

THANKS FOR VISITING US

"""

print(detailed_bill)