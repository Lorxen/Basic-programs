# Simple function to know if a year is a leap year or not

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap year')
            else:
                print('not leap year')
        else:
            print('Leap year')
    else:
        print('Not leap year')


is_leap_year(2000)
