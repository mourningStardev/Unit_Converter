# Basic Unit converter #


# Base Unit Factors (Arrays)
units = {
    "LENGTH": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    },
    "AREA": {
        "square_meter": 1.0,
        "square_kilometer": 1e6,
        "square_cenTIMEter": 0.0001,
        "square_millimeter": 1e-6,
        "hectare": 10000.0,
        "acre": 4046.86,
    },
    "VOLUME": {
        "cubic_meter": 1.0,
        "liter": 0.001,
        "milliliter": 1e-6,
        "cubic_centimeter": 1e-6,
        "cubic_inch": 1.6387e-5,
        "cubic_foot": 0.0283168,
        "gallon": 0.00378541,
    },
    "TIME": {
        "second": 1.0,
        "minute": 60.0,
        "hour": 3600.0,
        "day": 86400.0,
        "week": 604800.0,
    },
    "WEIGHT": {
        "kilogram": 1.0,
        "gram": 0.001,
        "milligram": 1e-6,
        "ton": 1000.0,
        "pound": 0.453592,
        "ounce": 0.0283495,
    },
}

print("Welcome to the Unit Converter!")
print("GROUP 8: JUMAWAN, DAGONDONG, FERNANDEZ, ACOSTA")

# --- Simple Flow with one category ---
def convt(category, fromUnit, toUnit, value):
    if category not in units:
        return "Invalid category"
    if fromUnit not in units[category] or toUnit not in units[category]:
        return "Invalid unit"
    
    base_value = value * units[category][fromUnit]
    converted_value = base_value / units[category][toUnit]
    return converted_value

# --- Interactive Flow with two categories ---
def convt(cat_from, fromUnit, cat_to, toUnit, value):
    # Validate categories
    if cat_from not in units or cat_to not in units:
        return "Invalid category"
    if fromUnit not in units[cat_from] or toUnit not in units[cat_to]:
        return "Invalid unit"

    # convt source → base (SI) → target
    base_value = value * units[cat_from][fromUnit]   # step 1: to SI base
    converted_value = base_value / units[cat_to][toUnit]  # step 2: to target
    return converted_value


# --- User Flow ---
cat_from = input("Choose FROM category (LENGTH, AREA, VOLUME, TIME, WEIGHT): ").lower()
print("Available units:", ", ".join(units[cat_from].keys()))
fromUnit = input("Enter the unit to convert FROM: ").lower()

cat_to = input("Choose TO category (LENGTH, AREA, VOLUME, TIME, WEIGHT): ").lower()
print("Available units:", ", ".join(units[cat_to].keys()))
toUnit = input("Enter the unit to convert TO: ").lower()

value = float(input("Enter the value: "))

result = convt(cat_from, fromUnit, cat_to, toUnit, value)
print(f"{value} {fromUnit} ({cat_from}) = {result} {toUnit} ({cat_to})")
