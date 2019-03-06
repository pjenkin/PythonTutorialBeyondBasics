correct_password = 'python123'
name = input('Enter name: ')
password = input('Enter password: ')

while correct_password != password:
    password = input('Wrong password! Enter correct password: ')

message = 'Hello {0} Logged in with password {1}'.format(name, password)
print(message)
