import time
# your code goes here!
def countdown(self):
    while self >= 0 :
        if self > 0:
            print(f'{self} SECOND(S)!')
            self -= 1
        elif self == 0:
            print('HAPPY NEW YEAR!')
            self -=1

def countdown_with_sleep(self):
    while self >= 0 :
        time.sleep(1)
        if self > 0:
            print(f'{self} SECOND(S)!')
            self -= 1
        elif self == 0:
            print('HAPPY NEW YEAR!')
            self -=1