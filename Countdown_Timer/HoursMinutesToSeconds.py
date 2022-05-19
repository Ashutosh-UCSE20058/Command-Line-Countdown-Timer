
#function to convert hours into seconds
def HoursToSeconds(hours):
    seconds = hours * 60 * 60
    print(f"The hours in seconds will be: {seconds} seconds")

# function to convert minutes into seconds

def MinutesToSeconds(minutes):
    seconds = minutes * 60
    print(f"The minutes in seconds will be: {seconds} seconds")

if __name__=="__main__":
    hours = int(input("Enter the hours that you want to convert into seconds: "))
    HoursToSeconds(hours)

    print("\n")
    
    minutes = int(input("Enter the minutes that you want to convert into seconds:  "))
    MinutesToSeconds(minutes)


