#Program 3: Temperature Alert System
temperature = 38
unit = "C" # C for Celsius, F for Fahrenheit

if unit == "C":
    print("Temperature in Celsius")

    if temperature <= 0:
        print("FREEZING! Water freezes")
    elif temperature <= 30:
        print("Normal temperature range")
        if temperature >= 25:
            print("Warm day")
        elif temperature <= 10:
            print("Cold day")
    else:
        print("HOT! Temperature above 30°C")
        if temperature >= 40:
            print("EXTREME HEAT WARNING!")
        else:
            print("Heat alert: Stay hydrated")

else: # Fahrenheit
    print("Temperature in Fahrenheit")
    if temperature <= 32:
        print("FREEZING! Water freezes")
    elif temperature <= 86:
        print("Normal temperature range")
    else:
        print("HOT! Temperature above 86°F")
