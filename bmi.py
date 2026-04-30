def calculate_bmi(height, weight):
    bmi = weight / (height**2)

    print(f"BMI = {bmi:.2f}")

    if bmi < 18.5:
        print("You are 'Under Weight'.")
    
    elif bmi <= 25.0:
        print("You are 'Normal Weight'")

    else:
        print("You are 'Over Weight")


user_weight = input("Enter your weight: ")
user_height = input("Enter yout height: ")
calculate_bmi(float(user_height), float(user_weight))