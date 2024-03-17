import random

print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes': quit()
score = 0;


print('Okay! Let\'s play')


# Question 1
answer = input('What does CPU stand for? ')
if answer == 'Central Processing Unit':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 2
answer = input('What is the binary equivalent of the decimal number 10? ')
if answer == '1010':
    print('Correct answer!')
    score+=1
else:
    print('Incorrect Answer!')

# Question 3
answer = input('What does HTML stand for? ')
if answer == 'Hypertext Markup Language':
    print('Correct answer!')
    score+=1
else:
    print('Incorrect Answer!')

# Question 4
answer = input('What is the most popular programming language in 2021? ')
if answer == 'Python':
    print('Correct answer!')
    score+=1
else:
    print('Incorrect Answer!')

# Question 5
answer = input('What is the process of finding errors and fixing them within a program? ')
if answer == 'Debugging':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 6
answer = input('What is the OSI model? ')
if answer == 'Open Systems Interconnection model':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 7
answer = input('What is a DNS? ')
if answer == 'Domain Name System':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 8
answer = input('What is SQL used for? ')
if answer == 'Structured Query Language':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 9
answer = input('What is the full form of URL? ')
if answer == 'Uniform Resource Locator':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')

# Question 10
answer = input('What is a firewall? ')
if answer == 'A security system that monitors and controls incoming and outgoing network traffic':
    print('Correct answer!')
    score+=1;
else:
    print('Incorrect Answer!')
 

print ('Congratulations! You have successfully completed the quit with '+ str(score) + ' marks')