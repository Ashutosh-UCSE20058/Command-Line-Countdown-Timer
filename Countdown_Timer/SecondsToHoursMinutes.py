
import time

def time_conversion(seconds):
    sec_value = seconds % (24 * 3600)
    hours_value = sec_value // 3600
    sec_value = sec_value % 3600
    minutes = sec_value // 60
    sec_value = sec_value % 60
    print(f"Converted seconds in hours: {hours_value} hours")
    print(f"Converted seconds in minutes: {minutes} minutes")


if __name__=="__main__":
    input = 24472
    time_conversion(input)