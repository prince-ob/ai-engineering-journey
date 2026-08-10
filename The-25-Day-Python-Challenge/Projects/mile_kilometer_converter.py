# Constant
OFFSET = 1.609344

# User input
mile_to_kilometer = 10
kilometer_to_miles = 50

# Conversion
kilometer = mile_to_kilometer * OFFSET
# miles = kilometer_to_miles // OFFSET # This will retrun as an integer instead of float but because OFFSET is a float, it will return as a float
miles = kilometer_to_miles / OFFSET 
print(f"{mile_to_kilometer} mile -> {kilometer:.1f} kilomter")
print(f"{kilometer_to_miles} kilometer -> {miles:.1f} mile")