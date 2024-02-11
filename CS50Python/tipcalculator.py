def dollars_to_float(input_string: str) -> float:
    dollars = float(input_string.replace("$", ""))
    return dollars


def percent_to_float(inpout_string: str) -> float:
    percent = float(inpout_string.replace("%", "")) / 100
    return percent

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")