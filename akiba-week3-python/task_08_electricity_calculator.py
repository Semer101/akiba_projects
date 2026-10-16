def validate_units (units): #validate units consumed
    if units < 0:
        return None
    else:
        return True

def calculate_charge(units_used): #calculate charge for each tier
    if validate_units(units_used) == None:
        return None
    else:
        if units_used <= 50:
            units_charge = 0.5 * units_used

        elif units_used <= 150:
            units_charge = ((units_used - 50) * 0.75) + (0.5 * 50)
        
        else:
            units_charge = ((units_used - 150) * 1.20) + (100 * 0.75) + (0.5 * 50)

    return units_charge


def total_bill(units_used, service_fee=0): #calculate total bill by adding service fee
    charge = calculate_charge(units_used)
    if charge == None:
        return None

    return charge + service_fee

def billing_summary(units_used, service_fee=0): #print bill summary
    bill = total_bill(units_used, service_fee)

    if bill == None:
        print("Invalid units! Consumption cannot be negative.")
    else:
        print("\n===== ELECTRICITY BILL =====")
        print(f"Units consumed: {units_used}")
        print(f"Service fee: {service_fee:.2f} Birr")
        print(f"Total bill: {bill:.2f} Birr")


units_used = float(input("Enter electricity units consumed: "))
service_fee = 5

billing_summary(units_used, service_fee)
#billing_summary(units_used)