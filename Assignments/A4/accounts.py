
#!/usr/bin/python
'''Author: Eric Lee
Date: 12/3/2016
Description: command-line utility for account information
Python version: Python version 3.5.2
'''
import sys
import getopt
import os
import time
import random

test_file = open("test.txt", "r+")#Open file
text_in_file = test_file.readlines()#Read file
date = (time.strftime("%y.%m.%d"))
'''----------------------------------Test---------------------------------------------------
print (text_in_file[0]) #line 1
print (text_in_file[0].split(":")[0]) #First number
print (text_in_file[0].split(":")[1]) #Name
print (text_in_file[0].split(":",2)[2]) #Everything else
print (text_in_file[0].split(":")[2]) #YY.MM.DD
print (text_in_file[0].split(":")[3]) #Deposit/Withdraw
print (text_in_file[0].split(":")[4]) #Money
----------------------------------Test---------------------------------------------------'''
newid = []
sortedid = []
#Appending Name and ID's

'''
-------------------------------------Sorted ID-------------------------------------------
'''
for i in range(0,len(text_in_file)):
    id = [(text_in_file[i])]
    sortedid.extend(id)
use_sorted_id = (sorted(set(sortedid)))
#Adds the information from the file into an array and sorts, set it.
accUnrepeated = []
isFullValid = []

for line in use_sorted_id:
    accData = line.split(':')
    accId = int(accData[0])   
    accName = accData[1]
    accDate = accData[2]
    accTransaction = accData[3]
    accMoney = accData[4]
    #Get data for each section of the string that is divided by :
    accFullInfo = [accName, accId, accDate, accTransaction, accMoney] #Testing
    accInfo = [accName, accId]

    if accFullInfo not in isFullValid:
        isFullValid.append(accFullInfo)

    if accInfo not in accUnrepeated:
        accUnrepeated.append(accInfo)

#get the raw_input
print("Please raw_input -i, -h,-t or q to leave")
while True: #Loop program 
    c = raw_input()
    if c == "-i": #Remember to change this to -i
        while c != "q":
            print("Info")
            print("----")
            for i in range(0, len(text_in_file)): #Loop to add the users and id
                try:
                    print("%s) %s" %(i+1, accUnrepeated[i])) #Print the user Name - ID in numerical order from lowest to highest, no repeated
                except IndexError: #got list index out of range in here, didn't know why. It's the same loop as above
                    pass
                continue
            print("q)uit")
            x = raw_input("Enter Choice => ") #Get raw_input
            print("")
            if x == "q": #Close application
               sys.exit()
            #PRINT ONLY IF IS THE SAME TO THE VALUE
            Help = []
            for name in use_sorted_id:
                accData = name.split(':')
                accId = int(accData[0])
                same = accUnrepeated[int(x)-1][1]
         
                if same == accId:
                   Help.append(name)
                balance = 0    
                for log in Help:
                    accData = log.split(':')
                    if accData[3] == "D":
                        balance += float(accData[4])
                    else:
                        balance -= float(accData[4])
               
            try:
                print("     account #:", accUnrepeated[int(x)-1][1]) #Print the Users account number
                print("          name:", accUnrepeated[int(x)-1][0]) #Print the Users Name
                print("       balance:", balance) #Prints balance
            except IndexError: #got list index out of range in here, didn't know why. It's the same loop as above
            	pass
            continue 
            
    elif c == "-h": #Remember to change this to -h
        while c != "q":
            print("History")
            print("----")
            for i in range(0, len(text_in_file)):
                try:
                    print("%s) %s" %(i+1, accUnrepeated[i]))  #Add the users and id
                except IndexError: #got list index out of range in here, didn't know why. It's the same loop as above
                        pass
                continue
            print("q)uit")
            
            x = raw_input("Enter Choice => ")
            print("")
            if x == "q":
                sys.exit()
            #I should had made this a function 
            #PRINT ONLY IF IS THE SAME TO THE VALUE
            Help = []
            for name in use_sorted_id:
                accData = name.split(':')
                accId = int(accData[0])

                same = accUnrepeated[int(x)-1][1]
                if same == accId:
            	    Help.append(name)

            for log in Help:
                accData = log.split(":")
                
                if accData[3] == "D":
            	    print('\t%s deposit $%s' % (accData[2], accData[4]))
                else:
            	    print('\t%s withdraw $%s' % (accData[2], accData[4]))


    elif c == "-t":#Remember to change this to -t
        while c != "q":
            print("Insert transaction")
            print("----")
            for i in range(0, len(text_in_file)):
                try:
                    print("%s) %s" %(i+1, accUnrepeated[i])) #Add the users and id
                except IndexError: #got list index out of range in here, didn't know why. It's the same loop as above
                    pass
                continue
            print("c)reate account")
            print("q)uit")

            x = raw_input("Enter Choice => ")
            print("\n")
            if x == "q":
                sys.exit()
            if x == "c":
                random.seed(time.time())
                name = raw_input("Enter your name ")               

                newID = random.randint(1000, 9999)
                print("Hello %s your ID number is %s" % (name, newID))                  
                test_file.write("\n%s:%s:%s:%s:%s" % (newID, name, date, "D", 0))#Write into file  
                continue
            
            Help = []
            for name in use_sorted_id:
                accData = name.split(':')
                accId = int(accData[0])
                same = accUnrepeated[int(x)-1][1]
                if same == accId:
                    Help.append(name)                             
                #Change this format
            if x.isdigit():
                print("Do you want to Withdraw or Deposit?(w/d)")
                t = raw_input()
                                    
                if (t == "w" or "W"):
                    print("How much money do you want to withdraw?")
                    m = int(raw_input()) 
                    print("You are withdrawing $%s, are you sure?(y/n)" %(m))
                    answer = raw_input()
                    if answer == "y":
                        for log in Help:    
                            accData = log.split(":")
                        print("Thanks for your transaction of %s." % (m))
                        print('\t%s withdraw $%s' % (date, m))
                        test_file.write("\n%s:%s:%s:%s:%s" % (accData[0], accData[1], date, "W", m))                                
                    elif answer == "n":
                        print("Thanks, we are now closing this")
                    else:
                        print("raw_input not recognized, try y or n.")
                elif (t == "d" or "D"):
                    print("How much money do you want to deposit?")
                    m = int(raw_input()) #If the raw_input isn't a number, error will show
                    print("You are depositing $%s, are you sure?(y/n)" %(m))
                    answer = raw_input()
                    if answer == "y":
                        for log in Help:    
                            accData = log.split(":")
                        print("Thanks for your transaction of %s." % (m))
                        print('\t%s deposit $%s' % (date, m))
                        test_file.write("\n%s:%s:%s:%s:%s" % (accData[0], accData[1], date, "D", m))
                    elif answer == "n":
                        print("Thanks, we are now closing this. Please try again.") 
                    else:
                        print("raw_input not recognized, try (y) or (n) next time.")
    elif c == "-?":
        print("To use this program please enter one of the following commands.")
        print("-i: Will give you the information of users that you choose.")
        print("-h: Will give you the transaction history of any user you choose.")
        print("-t: Will allow you to create an account or to add/withdraw money from an account you choose.")
        sys.exit()                    
    elif c == "q":
        sys.exit()
    else:
        print("Please enter a value that is valid.")

test_file.close()
