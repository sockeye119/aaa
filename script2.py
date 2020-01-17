
from food import Food
from food import Dressing
from food import Topping
from food import AddOn
from food import Side
from food import Dessert
from drink import Drink
from menu_item import MenuItem
#---------------------------------------------------------------------

#Restaurant 0: High Five Salad
food1 = Food('High Five Power Salad', 1580, 476)
food2 = Food('Smoked Duck & Honey Nut Salad', 1080, 220)
food3 = Food("Grilled Chicken & Egg Salad", 980, 262)
food4 = Food('Prosciutto & Mimolette Cheese Salad', 980, 139)
food5 = Food('Garlic Shrimp Salad', 1280, 113)

foods_res0 = [food1, food2, food3, food4, food5]

dressing1 = Dressing('Classic Caesar',0,73)
dressing2 = Dressing('Onion Soy',0,107)
dressing3 = Dressing('Creamy Seasame',0,67)
dressing4 = Dressing('Honey Mustard',0,127)
dressing5 = Dressing('Balsamic Vinaigrette',0,127)

dressings_res0 = [dressing1, dressing2, dressing3, dressing4, dressing5]

topping1 = Topping('Quinoa', 200, 14)
topping2 = Topping('Boiled Egg', 100, 97)
topping3 = Topping('Crouton', 100, 41)
topping4 = Topping('Mixed Nuts', 100, 23)
topping5 = Topping('Avocado', 250, 109)

toppings_res0 = [topping1, topping2, topping3, topping4, topping5] 

addon1 = AddOn('Green Smoothie', 360, 126)
addon2 = AddOn('Bread', 80, 100)
addon3 = AddOn('Homemade Soup', 360, 234)
addon4 = AddOn('Iced Coffee', 100, 15)
addon5 = AddOn('Seasonal Smoothie', 500, 245)

addons_res0 = [addon1, addon2, addon3, addon4, addon5] 

#Restaurant 1: Thaliya
food1 = Food('Thaliya Bento', 680, 870)
food2 = Food('Indian Curry Box', 500, 650)
food3 = Food('Keema Curry Lunch Box', 720, 760)
food4 = Food('Chicken Pakora Lunch Box', 720, 650)
food5 = Food('Tandori Chicken Lunch Box', 1020, 870)

foods_res1 = [food1, food2, food3, food4, food5] 

side1 = Side('Gorgonzola Cheese Naan', 350, 300)
side2 = Side('Seasame Naan', 300, 240)
side3 = Side('Tandori Chicken Salad', 460, 330)
side4 = Side('Cheese Naan', 250, 300)
side5 = Side('Indian French Fries', 280, 250)

sides_res1 = [side1, side2, side3, side4, side5] 

drink1 = Drink('Mango Lassi', 350, 300)
drink2 = Drink('Chai Milk Tea Tapioca', 350, 300)
drink3 = Drink('Strawberry Lassi', 350, 300)
drink4 = Drink('Melon Milk Tapioca', 350, 300)
drink5 = Drink('Matcha Lassi', 350, 300)

drinks_res1 = [drink1, drink2, drink3, drink4, drink5]

#Restaurant 2: Toden Table
food1 = Food('Miso Soup with Pork and Vegetables Set Menu', 1000, 510)
food2 = Food('Chicken and Deep-fried Tofu Set Menu ', 1000, 400)
food3 = Food('Grilled Saba Fish Set Menu', 1100, 550)
food4 = Food('Deep-fried Oyster Set Menu', 1200, 620)
food5 = Food('Curry Rice', 900, 600)

foods_res2 = [food1, food2, food3, food4, food5]

drink1 = Drink('100% Apple Juice', 500, 50)
drink2 = Drink('100% Mikan Juice', 500, 50)
drink3 = Drink(' Ginger Soda', 400, 40)

drinks_res2 = [drink1, drink2, drink3]

#Restaurant 3: Dondondon
food1 = Food('Bibimpa', 600, 600)
food2 = Food('Shin Ramen Noodles Set Menu', 600, 700)
food3 = Food('Cold Noodles ', 800, 500)
food4 = Food('Spicy Tofu Soup', 800, 520)
food5 = Food('Bulgogi Set Menu', 1000, 890)
             
foods_res3 = [food1, food2, food3, food4, food5]

drink1 = Drink('Mineral Water', 200, 0)
drink2 = Drink('Oolong Tea', 200, 0)

drinks_res3= [drink1, drink2]

#Restaurant 4: Good Morning Cafe 
food1 = Food('GMC Omelette Rice (soup set)', 900, 630)
food2 = Food('GMC Burger (soup and french fries set)', 1100, 550)
food3 = Food('Tomato Spaghettini with Bacon and Onions', 950, 590)
food4 = Food('Bolognese (soup and french fries set)', 1050, 690)
food5 = Food('Carbonara (soup and french fries set)', 1100, 730)

foods_res4 = [food1, food2, food3, food4, food5]

drink1 = Drink('Coffee', 150, 0)
drink2 = Drink('Tea', 150, 2)
drink3 = Drink('Coca Cola', 200, 140)
drink3 = Drink('Ginger Ale', 200, 140) 
drink3 = Drink('Pineapple Juice', 200, 133)
               
drinks_res4 = [drink1, drink2, drink3, drink4, drink5]

dessert1 = Dessert('Vanilla caramel angel food cake', 600, 200)
dessert2 = Dessert('Pistachio and cherry tart', 700, 340)
dessert3 = Dessert('Double cheese cake', 600, 320)
dessert4 = Dessert('Mille crêpes with praline', 650, 340)
dessert5 = Dessert('Gâteau au Chocolat', 650, 380)

desserts_res4 = [dessert1, dessert2, dessert3, dessert4, dessert5]

#Restaurant 5: Where is a dog? 
food1 = Food('Asian Curry Plate (soup and mini desert set)', 1200, 590)
food2 = Food(' Rice Bowl with Vegetables (soup and mini desert set)', 1200, 370)
food3 = Food('Pizza Toast (soup and mini desert set)', 1000, 310)
food4 = Food('Vegan Plate (soup and mini dessert set)', 1200, 310)
food5 = Food('Herb Fragrant Salt Pork Bowl (soup and mini dessert set)', 1000, 680)

foods_res5 = [food1, food2, food3, food4, food5]

drink1 = Drink('Decaf Coffee', 450, 0)
drink2 = Drink('Organic Black Tea', 450, 0)
drink3 = Drink('Morinaga Tea', 500, 0)
drink3 = Drink('Citrus Unshiu Juice', 450, 35) 
drink3 = Drink('Perrier', 350, 0)
               
drinks_res5 = [drink1, drink2, drink3, drink4, drink5]

dessert1 = Dessert('Pancake with Vegan Butter and Fruits', 880, 105)
dessert2 = Dessert('Waffles with Soy Milk Whipped Cream and Fruits', 880, 180)
dessert3 = Dessert('Brownie Soy Milk Whipped', 650, 200)
dessert4 = Dessert('Clafoutis with Shanti Sauce', 700, 250)
dessert5 = Dessert('Coconut Kudzu Pudding', 650, 140)

desserts_res5 = [dessert1, dessert2, dessert3, dessert4, dessert5]

#---------------------------------------------------------------------

#function to print menu for each food type for each restaurant)
def printMenu(restaurant,menuName,foodType,foodTypeString):
    print()
    print('----------------------------------------------------------')
    print(restaurant + ' *' + foodTypeString + ' MENU*')
    print('----------------------------------------------------------')
    index = 0
    for x in menuName:
        print(str(index) + '. ' + foodType.info(x))
        index += 1

#function to print instructions for selection of item from menu
#created to loop so that invalid inputs cannot be entered

def printSelectionInstruction(menuName):
    print()
    print('- Keep empty if no items are desired from the menu -')
    food_choice = input('Please select a number from the menu: ')

    while food_choice.isalpha():
        print("-Please insert a number corresponding to a restaurant-")
        print()
        food_choice = input('Please select a number from the menu: ')

    while int(food_choice) > index or int(food_choice)< 0:
        print("-Please insert a number corresponding to a restaurant-")
        print()
        food_choice = input('Please select a number from the menu: ')

    selected_food = menuName[int(food_choice)]
    food_count = input('Please type in the desired quantity: ')

    while food_count.isalpha():
        print("-Please insert a number corresponding to a restaurant-")
        print()
        food_count = input('Please type in the desired quantity: ')

    while int(food_count) > index or int(food_count)< 0:
        print("-Please insert a number corresponding to a restaurant-")
        print()
        food_count = input('Please type in the desired quantity: ')
        
    int(food_count)
    print()
        

cart = ()        
total = ()
print('----------------------------------------------------------')
print('---------------Hello, welcome to W-Delivers!--------------')
print('----------------------------------------------------------')
input('Please insert your name: ')
input('Please insert your faculty: ')
input('PLease insert your grade: ')
input('Please state the building and classroom number of pick up location (Must be on Waseda or Toyama Campus): ')
input('Please insert preferred time of pickup : ')
print('----------------------------------------------------------')
print('Please note that the only payment method available is CASH')
print('----------------------------------------------------------')

restaurants = {'toden table': '(Japanese)',
                'dondondon': '(Korean)',
                'highfive salad': '(Salad)',
                'thaliya': '(Indian)',
                'Good morning cafe': '(Western-style)',
                'Where is a dog?': '(Gluten-free)'
               }

print('Restaurant Options: ')
index = 0
for key,value in restaurants.items():
    print(str(index) + '.' + key, ' ', value)
    index += 1
    
print('----------------------------------------------------------')

restaurant_choice = input('Please select a number from the list of restaurants: ')

while restaurant_choice.isalpha():
    print("-Please insert a number corresponding to a restaurant-")
    print()
    restaurant_choice = input('Please select a number from the list of restaurants: ')
    
while int(restaurant_choice)>index or int(restaurant_choice)< 0:
    print("-Please insert a number corresponding to a restaurant-")
    print()
    restaurant_choice = input('Please select a number from the list of restaurants: ')
    
while 0 <= int(restaurant_choice) <= 5 :
    if restaurant_choice == "0":
        printMenu("High Five Salad",foods_res0,Food, "FOOD")
        printSelectionInstruction(foods_res0)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()

        printMenu("High Five Salad",dressings_res0,Dressing, "DRESSING")
        printSelectionInstruction(foods_res0)
        
        printMenu("High Five Salad", toppings_res0,Topping, "TOPPING")
        printSelectionInstruction(toppings_res0)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()

        printMenu("High Five Salad", addons_res1,AddOn, "ADD-ON")
        printSelectionInstruction(addons_res1)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')

    if restaurant_choice == "1":
        printMenu("Thaliya", foods_res1,Food, "FOOD")
        printSelectionInstruction(foods_res1)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Thaliya", sides_res1,Side, "SIDE")
        printSelectionInstruction(sides_res1)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()

        printMenu("Thaliya", drinks_res1,Drink, "DRINK")
        printSelectionInstruction(drinks_res1)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')
    if restaurant_choice == "2":
        printMenu("Toden Table", foods_res2,Food, "FOOD")
        printSelectionInstruction(foods_res2)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Toden Table", drinks_res2,Drink, "DRINK")
        printSelectionInstruction(drinks_res2)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')
        
    if restaurant_choice == "3":
        printMenu("Dondondon", foods_res3,Food, "FOOD")
        printSelectionInstruction(foods_res3)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Dondondon", drinks_res3,Drink, "DRINK")
        printSelectionInstruction(drinks_res3)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')
        
    if restaurant_choice == "4":
        printMenu("Good Morning Cafe", foods_res4,Food, "FOOD")
        printSelectionInstruction(foods_res4)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Good Morning Cafe", drinks_res4,Drink, "DRINK")
        printSelectionInstruction(drinks_res4)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Good Morning Cafe", desserts_res4,Dessert, "DESSERT")
        printSelectionInstruction(desserts_res4)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')
    if restaurant_choice == "5":
        printMenu("Where is a Dog?", foods_res5,Food, "FOOD")
        printSelectionInstruction(foods_res5)
        
        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Where is a Dog?", drinks_res5,Drink, "DRINK")
        printSelectionInstruction(drinks_res5)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        
        printMenu("Where is a Dog?", desserts_res5,Dessert, "DESSERT")
        printSelectionInstruction(desserts_res5)

        total += selected_food.get_total_price(food_count)
        print(total)
        print()
        print('----------------------------------------------------------')
    
    



food_order = int(input('食べ物の番号を選択してください: '))
selected_food = foods[food_order]

drink_order = int(input('飲み物の番号を選択してください: '))
selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
print('合計は' + str(result) + '円です')


