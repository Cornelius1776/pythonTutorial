# logical operators check how many conditional statement are true. they are; and, or, not.

weather_temperature = int(input("what is the temperature in Nigeria?"))

if weather_temperature > 25 and weather_temperature < 35:
    print("The weather is warm today!")
elif not (weather_temperature > 20):
    print("The weather is cold!")
elif weather_temperature < 10 or weather_temperature > 35:
    print("The weather is extreme")
