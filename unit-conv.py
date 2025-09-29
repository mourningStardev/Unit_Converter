# Basic Unit Converter using only conditional statements, user input, and basic math

print("Welcome to the Unit Converter!")
category = input("Input Base factor >> ")

if category == "length":
    print("Units: METER, KILOMETER, CENTIMETER, MILLIMETER, MILE, YARD, FOOT, INCH")
    from_unit = input("From unit: ")
    to_unit = input("To unit: ")
    value = float(input("Enter value: "))

    # Convert from_unit to meters
    if from_unit == "meter":
        meters = value
    elif from_unit == "kilometer":
        meters = value * 1000
    elif from_unit == "centimeter":
        meters = value * 0.01
    elif from_unit == "millimeter":
        meters = value * 0.001
    elif from_unit == "mile":
        meters = value * 1609.34
    elif from_unit == "yard":
        meters = value * 0.9144
    elif from_unit == "foot":
        meters = value * 0.3048
    elif from_unit == "inch":
        meters = value * 0.0254
    else:
        print("Unsupported unit.")
        exit()

    # Convert meters to target unit
    if to_unit == "meter":
        result = meters
    elif to_unit == "kilometer":
        result = meters / 1000
    elif to_unit == "centimeter":
        result = meters / 0.01
    elif to_unit == "millimeter":
        result = meters / 0.001
    elif to_unit == "mile":
        result = meters / 1609.34
    elif to_unit == "yard":
        result = meters / 0.9144
    elif to_unit == "foot":
        result = meters / 0.3048
    elif to_unit == "inch":
        result = meters / 0.0254
    else:
        print("Unsupported unit.")
        exit()

    print(f"{value} {from_unit} = {result} {to_unit}")
