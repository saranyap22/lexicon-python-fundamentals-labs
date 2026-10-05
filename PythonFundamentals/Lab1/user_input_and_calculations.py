""" This module contains functions supporting arithmatic operatoin based on user input data """
from datetime import date


def calculate_age(name, year_of_birth):
    """ Function calculate approximate age based on user input name and year of borth"""
    year = int(year_of_birth)
    age = date.today().year - year
    print(f"Current age of {name.strip()} is {age}")


def calculate_final_price(item_price, discount_percentage):
    """ Function to calculate Final price after applying diccount on item price """
    final_price = item_price - item_price * discount_percentage / 100
    print(f"Final item price: {final_price}")


def convert_celcius_to_Fahrenheit(celcius):
    """Function to convert temperature in celcius to Fahrenheit"""
    fahrenheit = celcius * 9 / 5 + 32
    print(f"Temperature in celcius: {fahrenheit}")


def calculate_area_and_perimeter(length, width):
    """ Function to calculate area and perimeter of rectangle"""
    area = length * width
    perimeter = 2 * area
    print(f"Area: {area}, Perimeter: {perimeter}")


length = input("Enter length of rectangle:")
width = input("Enter width of rectangle:")
# Allowing input without conversion will result in TypeError (Can't multiply by sequence of non int() with str)
# While having conversion with Invalid numeric input like "sas" will result in ValueError (Cannot convert String to float)
calculate_area_and_perimeter(float(length), float(width))

tem_in_celcius = input("Enter temperature in celcius:")
convert_celcius_to_Fahrenheit(float(tem_in_celcius))

name = input("Enter your name:")
year_of_birth = input("Enter your year of birth:")
calculate_age(name, year_of_birth)

item_price = input("Enter price of item:")
discount_percentage = input("Enter discount percentage:")
calculate_final_price(float(item_price), float(discount_percentage))
