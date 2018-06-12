'''
Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
'''

first_name=input('Enter First name: ')
last_name =input('Please Enter LAst Name: ')

print('{1} {0}'.format(first_name,last_name))