#!/usr/bin/python
import os
import datetime

os.system('cls')

count = 0

def menu():
	while True:
		# displays menu
	    print('{0:^50s}'.format('MENU'))
	    print('{0:^50s}'.format('----'))
	    print('{0:>52s}'.format('V - Print every third character in an expression'))
	    print('{0:>56s}'.format('R - Read an input file and count the number of words'))
	    print('{0:>50s}'.format('H - Read an HTML url and save the file locally'))
	    print('{0:>53s}'.format('C - Print the current directory location of where'))
	    print('{0:>31s}'.format('the script is executing'))
	    print('{0:>65s}'.format('F - Read an input file, perform calculations, and format data'))
	    print('{0:>43s}'.format('D - Read an HTML url and count the tags'))
	    print('{0:>46s}'.format('A - Given a date, count the number of days'))
	    print('{0:>59s}'.format('P - Given an input string proper case each first letter'))
	    print('{0:>12s}'.format('Q - Quit'))
	    print()
	    option = input('OPTION: ').upper().strip()
	    print()

	    if option == 'V':
	    	optionV();
	    elif option == 'R':
	    	optionR();
	    elif option == 'H':
	    	optionH();
	    elif option == 'C':
    		optionC();
	    elif option == 'F':
	    	optionF();
	    elif option == 'D':
	    	optionD();
	    elif option == 'A':
    		optionA();
	    elif option == 'P':
	    	optionP();
	    elif option == 'Q':
	        exit()
	    else:
	        continue

def optionV():
    expr = input('Enter an expression (or M for main menu): ').strip()
    while expr.upper() != 'M':
        if len(expr) < 10: # check for expressions less than 10 characters
            print('Expression must be at least ten characters long.\n')
        else:
            expr = expr.replace(' ', '').replace('\t', '') # strips expression of white space
            print(expr[2:3] + expr[5::3]) # prints every third character in expr
        expr = input('Enter an expression (or M for main menu): ').strip()
    os.system('cls')

def optionR():
    filename = input('Enter name of file (or M for main menu): ').strip()
    while filename.upper() != 'M':
        try:
            file = open(os.getcwd() + '\\' + filename).read()
            print('Word count: ', len(file.split())) # count number of words
        except:
            print('File not found.')
        filename = input('\nEnter name of file (or M for main menu): ').strip()
    os.system('cls')	

def optionH():
    url = input('Enter URL (or M for main menu): ').strip()
    while url.upper() != 'M':
        from urllib.request import urlopen
        localfile = open('data.html', 'w') # create writable file object
        try:
            for line in urlopen(url):
                localfile.write(str(line.decode()) + '\n') # write html to local file
        except:
            print('URL not found.')
        url = input('Enter URL (or M for main menu): ').strip()
    os.system('cls')

def optionC():
    print(os.getcwd())
    input('\nPress Enter to continue...')
    os.system('cls')	

def optionF():
    filename = input('Enter name of csv file (or M for main menu): ').strip()
    while filename.upper() != 'M':
        try:
            csvfile = open(os.getcwd() + '\\' + filename).readlines() # read line of file
            templist = []
            print()
            print('%-11s %-13s %-10s %-7s %-11s %-10s %-10s' 
                % ('Hourly Pay', 'Hours Worked', '1st * 2nd', 'FICO', 'Exemptions', 'Gross Pay', 'Net Pay'))
            for row in csvfile:
                templist = row.split(',') # csv data into temporary list
                hourlypay = float(templist[0])
                hoursworked = int(templist[1])
                fico = float(templist[3])
                if fico >= 1:
                    fico = float(templist[3]) * .01
                exempt = float(templist[4])
                grosspay = hourlypay * hoursworked
                adjustedgross = grosspay - exempt
                netpay = adjustedgross - (adjustedgross * fico)
                print('%-11.2f %-13d %-10.2f %-7.4f %-11.2f %-10.2f %-10.2f' 
                    % (hourlypay, hoursworked, grosspay, float(templist[3]), exempt, adjustedgross, netpay))
            print()
        except:
            print('File not found.')
        filename = input('Enter name of csv file (or M for main menu): ').strip()
    os.system('cls')	

def optionD():
    url = input('Enter URL (or M for main menu): ').strip()
    while url.upper() != 'M':
        from urllib.request import urlopen
        try:
            with urlopen(url) as response:
                for line in response:
                    for x in line.decode():
                        if x in '<':
                            count += 1
            print('Number of tags:', count)
            count = 0
        except:
            print("Invalid URL.")
        url = input('Enter URL (or M for main menu): ').strip()
    os.system('cls')

def optionA():
    date = input('Enter date (or M for main menu): ').strip()
    while date.upper() != 'M':
        date = date.replace('/', '-').replace(' ', '-').split('-') # replace tokens with '-'
        today = datetime.datetime.now() # create object for today's date
        try:
            userdate = datetime.datetime(int(date[2]), int(date[0]), int(date[1])) # create object for user's date
            numberOfDays = today - userdate # subtracts today's date from user's date
            print('Days:', abs(numberOfDays.days)) # print absolute value of difference of days
        except:
            print('Invalid date.')
        date = input('\nEnter month (or M for main menu): ').strip()
    os.system('cls')

def optionP():
    string = input("Enter string (or M for main menu): ").strip()
    while string.upper() != 'M':
        for word in string.split():
            print(word[:1].upper() + word[1:], sep=' ', end=' ') # uppercase first letter in each word
        string = input("\n\nEnter string (or M for main menu): ").strip()
    os.system('cls')

if __name__ == '__main__':
	menu();
