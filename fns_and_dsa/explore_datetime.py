from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ",current_date.strftime("%y-%m-%d %H:%M:%S"))
display_current_datetime()

def calculate_future_date():
    current_date = datetime.now()
    future_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(future_date)
    print("Future date: ", future_date.strftime("%y-%m-%d %H:%M:%S"))

calculate_future_date()