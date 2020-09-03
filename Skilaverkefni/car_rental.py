# Nafn: Yazmin Lilja Rós Guðjónsdóttir
# Hópur 5
print("Welcome to car rentals!")

# spyr hvort vilji halda áfram
con = input("Would you like to continue (y/n)? ")

# geri while lykkju til að endurtaka þar til svarið verður n
while con == 'y':
    # spyr um kóða
    customer_code = input("Customer code (b or d): ")
    # geri if lykkju eftir því hvort kóði sé b eða d
    if customer_code == 'b':
        # spyr u daga og mílur til að ná að reikna
        days = input("Number of days: ")
        days_int = int(days) # breyti í integer
        odo_start = input("Odometer reading at the start: ")
        odo_s_int = int(odo_start)
        odo_end = input("Odometer reading at the end: ")
        odo_e_int = int(odo_end)
        miles = odo_e_int - odo_s_int
        print("Miles driven: ",miles) # reikna milurnar
        amount = (40 * days_int) + (0.25 * miles)
        r_amount = round(amount,1)
        print("Amount due: ", r_amount)
    elif customer_code == 'd':  
        # svipað og b kóðinn
        days = input("Number of days: ")
        days_int = int(days)
        odo_start = input("Odometer reading at the start: ")
        odo_s_int = int(odo_start)
        odo_end = input("Odometer reading at the end: ")
        odo_e_int = int(odo_end)
        miles = odo_e_int - odo_s_int
        print("Miles driven: ",miles)
        miles = miles/days_int
        # geri if lykkju til að reikna mílurnar sem fara yfir 100 á dag
        if miles > 100:
            miles = miles - 100
            amount = (60 * days_int) + ((0.25 * miles)*days_int)
            r_amount = round(amount,1)
        else:
            amount = (60 * days_int)
            r_amount = round(amount,1)
        print("Amount due: ",r_amount)
    # spyr aftur hvort vilji halda áfram svo while lykkjan verði ekki endalaus
    con = input("Would you like to continue (y/n)? ")
