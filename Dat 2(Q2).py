#Question - 2
#Check whether a string is a pangram
#OTP Generator Project
#6 Digit Characters OTP

import random as r
import string
length = 6
otp = ''

characters = string.ascii_letters + string.digits

for i in range(length):
    otp = otp + r.choice(characters)

print("OTP: ", otp)

#4 Digit Banking OTP

import random as r
import string
length = 4
otp = ''
 
digits = string.digits

for i in range(length):
    otp = otp + r.choice(digits)

print("OTP: ", otp)