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
