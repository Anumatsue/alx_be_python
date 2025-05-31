weather_1 = "sunny"
weather_2 = "rainy"
weather_3 = "cold"

weather_condition = str(input("Whats the weather like today?(sunny/rainy/cold): "))
if weather_condition == weather_1:
   print("Wear a t-shirt and sunglasses.")
elif weather_condition == weather_2:
   print("Don't forget your umbrella and a raincoat.")
elif weather_condition == weather_3:
   print("Make sure to wear a warm coat and a scarf.")

else:
   print("Sorry, I don't have recommendations for this weather.")