def calculate_letter_gread(score: int) -> str:
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


try:
    user_input = input("enter your gread (0-100):")
    grade = int(user_input)

    if grade < 0 or grade > 100:
        raise ValueError("grade must be between 0 and 100.")

    letter = calculate_letter_gread(grade)

except ValueError as ve:
    print(f"error {ve}")
else:
    print(f"your letter grade is:{letter}")
finally:
    print("thank you for using the grade calculate. goodbye!")
