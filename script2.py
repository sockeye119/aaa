
from food import Food
from drink import Drink
from Dressing import Dressing
from topping import Topping 
fromm addon import Addon
#---------------------------------------------------------------------

#Restaurant 2: 都電テーブル早稲田 Toden Table Waseda 
foods_2 = [['豚汁定食 (Miso Soup with Pork and Vegetables Set Menu)', 1000, 510],
           ['鶏と豆腐の揚げ出し定食　(Chicken and Deep-fried Tofu Set Menu)', 1000, 400],
           ['鯖の塩焼き (Grilled Saba Fish Set Menu)', 1100, 550],
           ['カキフライ定食 (Deep-fried Oyster Set Menu)', 1200, 620],
           ['カレーライス (Curry Rice)', 900, 600]
           ]

drinks_2 = [['100% Apple Juice', 500, 50],
            ['100% Mikan Juice', 500, 50],
            ['Ginger Soda', 400, 40],
            ]

#Restaurant 3: どんどんどんDon Don Don 
foods_3 = [['ビビンパ　(Bibimpa)', 600, 600],
           ['辛ラーメン定食 (Shin Ramen Noodles Set Menu)', 600, 700],
           ['冷麺　(Cold Noodles)', 800, 50],
           ['純豆腐チゲ　(Spicy Tofu Soup)', 800, 520],
           ['牛ブルゴキ定食　(Bulgogi Set Menu)', 1000, 890]
           ]

drinks_3 = [['Mineral Water', 200, 0],
            ['Oolong Tea', 200, 0],
            ]
#Restaurant 4: Good Morning Cafe 
foods_4 = [['GMC Omelette Rice (soup set)',900,630],
           ['GMC Burger (soup and french fries set)',1100,550],
           ['Tomato Spaghettini with Bacon and Onions',950,590],
           ['Bolognese (soup and french fries set)',1050,690],
           ['Carbonara (soup and french fries set)',1100,730]
           ]

drinks_4 = [['Coffee',150,0],
            ['Tea',150,2],
            ['Coca Cola',200,140],
            ['Ginger Ale',200,140],
            ['Pineapple Juice',200,133]
            ]
               
desserts_4 = [['Vanilla caramel angel food cake',600,200],
              ['Pistachio and cherry tart',700,340],
              ['Double cheese cake',600,320],
              ['Mille crêpes with praline',650,340],
              ['Gâteau au Chocolat',650,380]
              ]

#Restaurant 5: Where is a dog?
foods_5 = [['Asian Curry Plate (soup and mini desert set)',1200,590],
           ['Rice Bowl with Vegetables (soup and mini desert set)',1200,370],
           ['Pizza Toast (soup and mini desert set)',1000,310],
           ['Vegan Plate (soup and mini dessert set)',1200,310],
           ['Herb Fragrant Salt Pork Bowl (soup and mini dessert set)',1000,680]
           ]

drinks_5 = [['Decaf Coffee',450,0],
            ['Organic Black Tea',450,0],
            ['Morinaga Tea',500,0],
            ['Citrus Unshiu Juice',450,35],
            ['Perrier',350,0]
            ]

desserts_5 = [['Pancake with Vegan Butter and Fruits',880,105],
              ['Waffles with Soy Milk Whipped Cream and Fruits',880,180],
              ['Brownie Soy Milk Whipped',650,200],
              ['Clafoutis with Shanti Sauce',700,250],
              ['Coconut Kudzu Pudding',650,140]
              ]

#---------------------------------------------------------------------

def printMenu(restaurant,food_type,menu_name):
    print(restaurant + ' *' + food_type + ' MENU*')
    index = 0
    for i in menu_name:
        for j in i:
            print(str(index) + '. ' + str(j), end = ' ')
        index += 1
        print()
    print()
        

        
total = ()

print('Hello, welcome to W-Delivers!')
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

restaurant_choice = int(input('Please select a number from the list of restaurants: '))
print()
print('Keep empty if item is undesired')
if restaurant_choice == 4:
    printMenu("Good Morning Cafe", "FOOD", foods_4)
    food_choice = int(input('Please select a number from the menu: '))
    food_count = int(input('Please type in the desired quantity: '))
##    total += foods_4[food_choice][1]*food_count
##    print(total)
##    print()
    printMenu("Good Morning Cafe", "DRINKS", drinks_4)
    drink_choice = int(input('Please select a number from the menu: '))
    drink_count = int(input('Please type in the desired quantity: '))
    printMenu("Good Morning Cafe", "DESSERTS", desserts_4)
    dessert_choice = int(input('Please select a number from the menu: '))
    dessert_count = int(input('Please type in the desired quantity: '))
    print('----------------------------------------------------------')
if restaurant_choice == 5:
    printMenu("Where is a dog?", "FOOD", foods_5)
    food_choice = int(input('Please select a number from the menu: '))
    food_count = int(input('Please type in the desired quantity: '))
    print()
    printMenu("Where is a dog?", "DRINKS", drinks_5)
    drink_choice = int(input('Please select a number from the menu: '))
    drink_count = int(input('Please type in the desired quantity: '))
    print()
    printMenu("Where is a dog?", "DESSERTS", desserts_5)
    desserts_choice = int(input('Please select a number from the menu: '))
    desserts_count = int(input('Please type in the desired quantity: '))
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


