
import time

# function for hours countdown timer
# input: time in seconds
# if cannot convert time to seconds, time conversion program in given 

def countdown(time_input):
    while time_input:
        hours, minutes = divmod(time_input, 3600)
        minutes, seconds = divmod(minutes, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer, end = "\r")
        time.sleep(1)
        time_input -= 1

    print('Timer completed!')

if __name__=="__main__":
    input = input('Enter the hours in the state of seconds(2h = 2*3600s = 7200s): ')
    countdown(int(input))

