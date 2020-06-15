txt = input('Create password: ')
password = ''

for x in txt:
    if (x=='i'):
        password += '!'
    elif (x=='a'):
        password += '@'
    elif (x=='m'):
        password += 'M'
    elif (x=='B'):
        password +='8'
    elif (x=='o'):
        password += '.'
    else:
        password += x
password += 'q*s'

print('Your better password is:', password)
