# Temperature converter

# Constants
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

#User input
celsius_input = 20
fahrenheit_input = 85

# Conversions
converted_to_fahrenheit = (celsius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_celsius = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS
 
# Display 
# format specifier is used (:.1f) here and this tell python we want our value to one decimal
print(f"{celsius_input}C° -> {converted_to_fahrenheit:.1f}°F")
print(f"{fahrenheit_input}F ° -> {converted_to_celsius:.1f}°C")
