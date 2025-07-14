weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

if height <= 0:
    raise ValueError ("Height must be positive and greater than 0")
body_mass_index = weight / (height ** 2)

#rounds of the body index to 2 decimal places
body_mass_index = round(body_mass_index, 2)

print(f"Your body mass index is: {body_mass_index}")

#categorises your bmi
if body_mass_index < 18.5:
    print ("BMI falls under underweight category.")
elif 18.5 <= body_mass_index < 25:
    print ("BMI falls under Normal weight category.")
elif 25 <= body_mass_index < 30:
    print ("BMI falls under Overweight category.")
else:
    print ("BMI falls under the Obese category.")
    

       
        
        