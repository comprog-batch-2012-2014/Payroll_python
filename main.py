from Employee import *

def main():
    print("\t***** Payroll System *****\n")
    print("*********************************************************")
    print("*\tMilitary time\t\t\t\t\t*")
    print("*\tThis is time for morning 8:00 - 17:00\t\t*")
    print("* \tThis is time for overtime 18:00 - 23:00\t\t*")
    print("*********************************************************\n")
    e = Employee() # instanciate
    e.logIn()
    e.generateDTRRecord1() # save in file.txt the personal info of user
    for day in e.days:
        print("Today is", day)
        e.checkDay()
        e.work()
        e.askUserWantOt()
        e.generateDTRRecord2(day) # save in file.txt the time in time out record
    e.generateDTRRecord3() # save in file.txt the total of all salary and it's expenses
    print("The program is done, Please open the file", e.user_username + '.txt to see your DTR record')
    print("Thanks for using this program :)")
if '__main__' == __name__:
    main()
