correct_password = 'python123'
name = input('Enter name: ')
password = input('Enter password: ')

while correct_password != password:
    password = input('Wrong password! Enter correct password: ')

strings = (name, password)

message = 'Hello {0} Logged in with password {1}'.format(strings[0], strings[1])
print(message)
