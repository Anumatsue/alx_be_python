from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ",current_date.strftime("%y-%m-%d %H:%M:%S"))
display_current_datetime()

def future_date_calculator():
    current_date = datetime.now()
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(future_date)
    print("Future date: ", future_date.strftime("%y-%m-%d %H:%M:%S"))

future_date_calculator()