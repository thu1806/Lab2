def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input()
    string_list = numbers.split(",")
    float_list = [float(i) for i in string_list]
    return float_list

def calc_average_temperature(list):
    average = sum(list) / len(list)
    return average

def find_min_max_temperature(list):
    sorted_list = sorted(list)
    min = sorted_list[0]
    max = sorted_list[-1]
    min_max = [min, max]
    return min_max

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temaperature")

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average_temp = calc_average_temperature(num_list)
    print(f"Average = {average_temp:.2f}")
    min_max_temp = find_min_max_temperature(num_list)
    print(f"Min = {min_max_temp[0]}, Max = {min_max_temp[1]}")

if __name__ == "__main__":
    main()

