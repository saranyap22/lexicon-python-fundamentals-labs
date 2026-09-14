# Seconds converter
total_seconds = input("Enter seconds: ").strip()
whole_hours = int(total_seconds) // 3600
remaining_minutes = (int(total_seconds) % 3600) // 60
remaining_seconds = int(total_seconds) % 60
print(f"Total Seconds: {total_seconds} | Whole Hours: {whole_hours} | Remaining Minutes: {remaining_minutes} | Remaining Seconds: {remaining_seconds}")


# From 4 digit integer extract and print each digit without converting number to a string
number = 1990
digits = []
while number > 0:
    digit = number % 10
    digits.insert(0, digit)
    number = number // 10
print(digits)

# Masking program
text = input("Enter you text to mask: ").strip()
masked_text = "**" + text[2:-2] + "**"
print(masked_text)

# Predict before running
# Given input number from user and divide by 6 and print results with 2 decimal point
number = 101
print(f"Output :{number/6: .2f}")

# What happens when print method has different types of arguments
number = 9
print("Welcome to Python class at:" + str(number))

# "Who is the black sheep" - find,
text = "who is the black sheep"
print(len(text.replace(" ", "")))  # 1) length without space -> return 31

# 2) find last 4 chars ->  return "is the black sheep"
print(text[4:])

# 3) what split [-3:3] -> returns "ehe"
print(text[-3:3])
