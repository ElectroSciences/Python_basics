import random

type = input("what type of password do you want? ")
length = input("How long do you want your password to be? ")
weakPassword = ''
mediumPassword = ''
strongPassword = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
specialChar = '1234567890`~!@£$%^&*()-_=+[{}]'
if (type == 'weak'):
    for i in range(int(length)):
        randChar = random.choice(lowercase)
        weakPassword = weakPassword + randChar
    print("weak Password: " + weakPassword)
if (type == 'medium'):
    for i in range(int(length)):
        randChar = random.choice(uppercase + lowercase)
        mediumPassword = mediumPassword + randChar
    print("medium Password: " + mediumPassword)
if (type == 'strong'):
    for i in range(int(length)):
        randChar = random.choice(lowercase + uppercase + specialChar)
        strongPassword = strongPassword + randChar
    print("strong password: " + strongPassword)
