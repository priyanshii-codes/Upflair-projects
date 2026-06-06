try:

    weight = float(input("Enter Your Weight in kg: "))
    height = float(input("Enter Your Height in meters: "))

    bmi = weight / (height * height)

    print("Your BMI is =", round(bmi, 2))

    if bmi < 18.5:
        print("You are Underweight")

    elif bmi >= 18.5 and bmi < 25:
        print("You have Normal Weight")

    elif bmi >= 25 and bmi < 30:
        print("You are Overweight")

    else:
        print("You are Obese")

except ValueError:
    print("Invalid Input! Please Enter Numbers Only.")