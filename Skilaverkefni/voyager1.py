# Nafn: Yazmin Lilja Rós Guðjónsdóttir
# Hópur: 5
# setja inn daga og breyta i float
days_str = input("Number of days after 9/25/09: ")
days_float = float(days_str)

# setja inn hvar sólin er í byrjun
sun = 16637000000

# reikna út miles á dag og setja í reikninga
miles_day = 917784

miles = (miles_day*days_float) + sun
miles_float = float(miles)

miles_round = round(miles_float)
print("Miles from the sun: ", miles_round)

# reikna kilometers
kilo = 1.609344
kilometer = kilo*miles_round
kilo_round = round(kilometer)
print('Kilometers from the sun: ', kilo_round)


# reikna AU
AU = 92955887.6
AU_float = float(AU)
AU_calc = miles_float/AU_float
AU_round = round(AU_calc)
print('AU from the sun: ', AU_round)

