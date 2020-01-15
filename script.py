from food import Food
from drink import Drink
from side import Side
from topping import Topping 
from dressing import Dressing
from addon import Addon

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

food1 = Food('サンドイッチ', 500, 330)
food2 = Food('チョコケーキ', 400, 450)
food3 = Food('シュークリーム', 200, 180)

foods = [food1, food2, food3]

drink1 = Drink('コーヒー', 300, 180)
drink2 = Drink('オレンジジュース', 200, 350)
drink3 = Drink('エスプレッソ', 300, 30)

drinks = [drink1, drink2, drink3]

print('食べ物メニュー')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('飲み物メニュー')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Insert number from food list: '))
selected_food = foods[food_order]

drink_order = int(input('Insert number from drink list: '))
selected_drink = drinks[drink_order]

# コンソールから入力を受け取り、変数countに代入してください
count = int(input('何セット買いますか？(3つ以上で1割引): '))

# selected_foodとselected_drinkのそれぞれに対して、get_total_priceメソッドを呼び出してください
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
print('The total is ' + str(result) + 'yen.')
