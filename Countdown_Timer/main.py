
import time

# function for a countdown timer
# this function only show the countdown for time upto minutes

def countdown(time_input):
    while time_input:
        minutes, seconds = divmod(time_input, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end = "\r")
        time.sleep(1)
        time_input -= 1

    print('Timer completed!')

if __name__=="__main__":
    input = input('Enter the time in seconds (1 minute = 60seconds): ')
    countdown(int(input))
