from Payroll import *

class Employee(Payroll):
    username = []
    password = []
    rate = []

    # constructor that pass all username, password and rate in attribute above /
    def __init__(self):
        file = open('employee.txt', 'r')
        for line in file:
            temp = line.split()
            self.username.append(temp[0].split(':')[1]) # save all username in username list variable
            self.password.append(temp[1].split(':')[1]) # save all password in password list variable
            self.rate.append(temp[2].split(':')[1]) # save all rate in rate list variable
        file.close()

    # login module for user /
    def logIn(self):
        isEmp = False
        username = input("Username: ")
        password = input("Password: ")
        for i in range(0, len(self.username)):
            if username == self.username[i] and password == self.password[i]: # checking account
                isEmp = True
                break
        if isEmp:
            self.user_username = self.username[i]
            self.user_password = self.password[i]
            self.user_rate = float(self.rate[i]) / 8
        else:
            print("Your account is not recognize, Please  check your account and try again")
            self.logIn()
