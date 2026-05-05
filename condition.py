#Program 1:BMI category Calculator
height=float(input("Enter height in meters: "))
Weight=float(input("Enter Weight in Kilograms: "))
BMI=Weight/(height)**2
print("BMI= ",BMI)
if BMI >=30 :
   print("Obesity")
elif 25<=BMI<=29:
    print("Overweight")
elif 18.5<=BMI<=25:
    print("Normal")
elif BMI<18.5:
     print("Underweight")

        
#program: find country of a city
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=input("Enter a city name: ").title()
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("City not found: ")


#3. check if two cities belong to same country
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city1 = input("Enter the first city name: ").title()
city2 = input("Enter the second city name: ").title()

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

elif city1 in India and city2 in India:
    print("Both cities are in India")

else:
    print("They don't belong to the same country")
