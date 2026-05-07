def calculate_bmi(height, weight):
    bmi = weight / (height**2)

    print(f"BMI = {bmi:.2f}")

    if bmi < 18.5:
        print("You are 'Under Weight'.")
        return -1
    
    elif bmi <= 25.0:
        print("You are 'Normal Weight'")
        return 0

    else:
        print("You are 'Over Weight")
        return 1

def main():
    user_weight = input("Enter your weight: ")
    user_height = input("Enter yout height: ")
    return_value = calculate_bmi(float(user_height), float(user_weight))
    print(f"Return Value: {return_value}")

if __name__ == "__main__":
    main()
