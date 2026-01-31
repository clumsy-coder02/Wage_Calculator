print() # spacing
print("Hourly Wage Calculator:")
print() # spacing

def wage_calculate():
    # starting time
    start_hour = int(input("Enter starting hour: "))
    start_minutes = int(input("Enter starting minutes: "))

    # ending time
    end_hour = int(input("Enter stopping hour: "))
    end_minutes = int(input("Enter stopping minutes: "))

    # hourly rate
    payment_per_hour = int(input("Enter your hourly rate: "))

    # working minutes
    total_working_minutes = end_minutes - start_minutes

    if total_working_minutes >= 60:
        # convert those minutes to hours
        hours = total_working_minutes // 60

        # calculate total hour worked
        total_working_hours = (end_hour - start_hour) + hours

        # calculate payment
        payment = total_working_hours * payment_per_hour
    else:
        # calculate total hour worked
        total_working_hours = end_hour - start_hour

        # calculate payment
        payment = total_working_hours * payment_per_hour

    print() # spacing

    # display the information
    info_1 = f"Worked from {start_hour:02d}:{start_minutes:02d} to {end_hour:02d}:{end_minutes:02d}\nTotal working hours: {total_working_hours} hrs"
    info_2 = f"Your hourly rate: ${payment_per_hour}\nPayment: ${payment}"

    return print(f"{info_1}\n{info_2}")


if __name__ == "__main__":
    wage_calculate()