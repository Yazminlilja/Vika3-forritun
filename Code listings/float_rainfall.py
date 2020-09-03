# Calculate rainfall in gallons for some number of inches on 1 acre

inches_str = input("How many inches of rain have fallen: ") # spurja um tölu
inches_float = float(inches_str) # breyta i float svo hægt að setja tugabrot
volume = (inches_float/12)*43560 # reikna rúmmál
gallons = volume * 7.48051945 # reikna gallons
print(inches_float," in. rain on 1 acre is", gallons, "gallons")

# hægt að setja inn tugabrot
