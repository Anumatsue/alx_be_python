'sunny' == "Wear a t-shirt and sunglasses."
'rainy' == "Don't forget your umbrella and a raincoat."
'cold' == "Make sure to wear a warm coat and a scarf."
weather = input("Whats's the weather like today? (sunny/rainy/cold): ")
if weather == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendation for this weather.")
