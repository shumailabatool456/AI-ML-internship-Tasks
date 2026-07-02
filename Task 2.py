
# SMART BMI & HEALTH RISK ANALYZER


print("=" * 45)
print("SMART BMI & HEALTH RISK ANALYZER")
print("=" * 45)
# Part 1 - Collect Patient Information
name = input("Enter Patient Name: ")
age = int(input("Enter Age (Years): "))
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (meters): "))

# Part 2 - Calculate BMI

bmi = weight / (height * height)

# Part 3 - Determine BMI Category

if bmi < 18.5:
    category = "Underweight"
    advice = "Increase calorie intake and consult a nutritionist."

elif bmi >= 18.5 and bmi <= 24.9:
    category = "Normal Weight"
    advice = "Maintain your current healthy lifestyle."

elif bmi >= 25 and bmi <= 29.9:
    category = "Overweight"
    advice = "Increase physical activity and improve diet."

else:
    category = "Obese"
    advice = "Consult a healthcare professional and follow a weight management plan."


# Part 4 - Assess Health Risk
# (Nested if-else)


if bmi > 30:
    if age > 40:
        health_risk = "High Health Risk"
    else:
        health_risk = "Normal Risk"
else:
    health_risk = "Normal Risk"

# Bonus Challenge 1
# Water Intake Calculator

water_intake = weight * 35

# Bonus Challenge 2
# Weight Difference Calculator

ideal_weight = 22 * (height * height)
weight_difference = weight - ideal_weight

# Part 5 - Display Health Report

print("\n")
print("=" * 45)
print("HEALTH REPORT")
print("=" * 45)

print(f"Patient Name              : {name}")
print(f"Age                       : {age} Years")
print(f"Weight                    : {weight:.1f} kg")
print(f"Height                    : {height:.2f} m")
print(f"Calculated BMI            : {bmi:.2f}")
print(f"BMI Category              : {category}")
print(f"Health Risk               : {health_risk}")

print(f"\nRecommended Water Intake  : {water_intake:.0f} ml/day")

print("\nWeight Information")
print(f"Current Weight            : {weight:.1f} kg")
print(f"Ideal Weight              : {ideal_weight:.1f} kg")
print(f"Weight Difference         : {weight_difference:.1f} kg")

print("\nHealth Recommendation")
print(advice)

print("=" * 45)
print("Thank you for using Smart BMI & Health Risk Analyzer")
print("=" * 45)