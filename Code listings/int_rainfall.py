# Calculate rainfall in gallons for some number of inches on 1 acre

inches_str = input("How many inches of rain have fallen: ") # spurja um tölu
inches_int = int(inches_str) # breyta i integer svo hægt að setja heila tölu
volume = (inches_int/12)*43560 # reikna rúmmál
gallons = volume * 7.48051945 # reikna gallons
print(inches_int," in. rain on 1 acre is", gallons, "gallons")

# ekki hægt að setja inn tugabrot
