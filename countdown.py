import time

def countdown(T):
    while T:
        mins, secs = divmod(T, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        T -= 1

    print('Out of time!!!!!!!!!!!')

T = input('Enter the time in seconds: ')

countdown(int(T))