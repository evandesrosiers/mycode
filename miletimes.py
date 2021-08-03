#!/usr/bin/env python3
#Author: Evan Sean DesRosiers
#Purpose: provide mile run time based on age


message = 'Based on your age, your recommended pace is '

# take age in years
age = int(input("What is your age in years?"))

# if input value was higher or equal to 25
if age <= 17:
    message = 'Please consult a physician before conducting intesne exercise as a minor'
elif age in range (18,29):
    message = message + 'under 10 minutes per mile'
elif age in range (30,49):
    message = message + 'between 10 and 12 minutes per mile'
else:
    message = message + 'over 12 minutes per mile'
print(message)

