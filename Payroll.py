from datetime import *

class Payroll:
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    isHoliday = bool
    time_in = "00:00"
    time_out = "00:00"
    time_in_ot = "00:00"
    time_out_ot = "00:00"
    user_username = '' # this is the current use of user
    user_password = '' # this is the current use of user
    user_rate = 0 # this is the rate of user per hour
    total_salary = 0

    def __init__(self):
        pass

    # asking user if holiday or not
    def checkDay(self):
        user_answer = ""
        while user_answer == "" or user_answer.lower() != 'y' \
              and user_answer.lower() != 'n':
            user_answer = input("Is it holiday today? [Y/N]")
        if user_answer.lower() == 'y':
            self.isHoliday = True
        else:
            self.isHoliday = False

    # time in and time out /
    def work(self):
        time_in = input("Time in: ")
        time_out = input("Time out: ")
        if ":" not in time_in or ":" not in time_out:
            print("Your time must be have ':'")
            self.work()
        elif not time_in.split(':')[0].isdigit() or \
             not time_out.split(':')[0].isdigit() or \
             not time_in.split(':')[1].isdigit() or \
             not time_out.split(':')[1].isdigit():
            print("Your time is not digit")
            self.work()
        elif int(time_in.split(':')[0]) > int(time_out.split(':')[0]) or \
             int(time_in.split(':')[0]) == int(time_out.split(':')[0]) and int(time_in.split(':')[1]) > int(time_out.split(':')[1]):
            print("Your time in is greather than time out")
            self.work()
        elif int(time_in.split(':')[0]) < 8 or int(time_in.split(':')[0]) > 17 or \
             int(time_in.split(':')[1]) < 0 or int(time_in.split(':')[1]) > 59 or \
             int(time_out.split(':')[0]) < 8 or int(time_out.split(':')[0]) > 17 or \
             int(time_out.split(':')[1]) < 0 or int(time_out.split(':')[1]) > 59 or \
             int(time_out.split(':')[0]) == 17 and int(time_out.split(':')[1]) < 60 and int(time_out.split(':')[1]) > 0:
            print("Your time is not base on instruction, read it again")
            self.work()
        else:
            self.time_in = time_in
            self.time_out = time_out

    # ask user if he/she want to overtime
    def askUserWantOt(self):
        if self.isHoliday == False:
            user_answer = ""
            while user_answer == "" or user_answer.lower() != 'y' \
                  and user_answer.lower() != 'n':
                user_answer = input("Do you want to overtime? [Y/N]")

            if user_answer.lower() == 'y':
                self.workOt()
            
    # time in and time out for ot /
    def workOt(self):
        time_in = input("Time in: ")
        time_out = input("Time out: ")
        if ":" not in time_in or ":" not in time_out:
            print("Your time must be have ':'")
            self.workOt()
        elif not time_in.split(':')[0].isdigit() or \
             not time_out.split(':')[0].isdigit() or \
             not time_in.split(':')[1].isdigit() or \
             not time_out.split(':')[1].isdigit():
            print("Your time is not digit")
            self.workOt()
        elif int(time_in.split(':')[0]) > int(time_out.split(':')[0]) or \
             int(time_in.split(':')[0]) == int(time_out.split(':')[0]) and int(time_in.split(':')[1]) > int(time_out.split(':')[1]):
            print("Your time in is greather than time out")
            self.workOt()
        elif int(time_in.split(':')[0]) < 18 or int(time_in.split(':')[0]) > 23 or \
             int(time_in.split(':')[1]) < 0 or int(time_in.split(':')[1]) > 59 or \
             int(time_out.split(':')[0]) < 18 or int(time_out.split(':')[0]) > 23 or \
             int(time_out.split(':')[1]) < 0 or int(time_out.split(':')[1]) > 59 or \
             int(time_out.split(':')[0]) == 23 and int(time_out.split(':')[1]) < 60 and int(time_out.split(':')[1]) > 0:
            print("Your time is not base on instruction, read it again")
            self.workOt()
        else:
            self.time_in_ot = time_in
            self.time_out_ot = time_out
            
   # reset to 00:00 all time, whether it is ot or not
    def resetTime(self):
        self.time_in = '00:00'
        self.time_out = '00:00'
        self.time_in_ot = '00:00'
        self.time_out_ot = '00:00'
   
    # get the total number of labor in minutes /
    def getMinuteOfLabor(self):
        try:
            hour = int(int(self.time_out.split(':')[0]) - int(self.time_in.split(':')[0]))
            minute = int(int(self.time_out.split(':')[1]) - int(self.time_in.split(':')[1]))
            if self.time_in_ot == "00:00":
                total_minute = 60 * (hour-1) + 60 + minute                
                return total_minute
            else:
                hour_ot = int(int(self.time_out_ot.split(':')[0]) - int(self.time_in_ot.split(':')[0]))
                minute_ot = int(int(self.time_out_ot.split(':')[1]) - int(self.time_in_ot.split(':')[1]))
                total_minute = 60 * ((hour + hour_ot) - 1) + 60 + (minute + minute_ot)
                return int(total_minute)
        except ValueError:
            print("You did not use the system properly, bye")
            return -1

    # checking if singular or plural /
    def getAppropriateWord(self, type, num):
        if type == 'hour':
            if num > 1:
                return num, "hours"
            elif num == 1 or num == 0:
                return num, "hour"
            else:
                return -1, "hour"
        elif type == 'minute':
            if num > 1:
                return num, "minutes"
            elif num == 1 or num == 0 :
                return num, "minute"
            else:
                return -1, "minute"
        else:
            return "Error", type

    # generate DTR Record / save /
    def generateDTRRecord1(self):
        time = datetime.now()
        file = open(self.user_username + '.txt', 'a')
        file.write('\t***** DTR RECORD *****\n');
        file.write('username: ' + self.user_username + "\t\t" + 'Date: ' + time.strftime('%B %d, %Y') + '\n')
        file.write('password: ' + self.user_password + '\n')
        file.write('rate: ' + str(float(self.user_rate * 8)) + ' per day' + '\n')
        file.write('\nLabor Record:\n')
        file.close()

    # another function for generating report /
    def generateDTRRecord2(self, day):
        if int(self.time_out.split(':')[0]) <= 12 and int(self.time_out.split(':')[0]) >= 8 or \
           int(self.time_in.split(':')[0]) > 12 and int(self.time_out.split(':')[0]) < 18:
           break_time = 0
        else:
            break_time = 1
        hour, minute = divmod(self.getMinuteOfLabor(), 60)
        salary = self.getAppropriateSalary(float((self.user_rate * (hour - break_time)) + \
                                            (self.user_rate * (minute / 60))))
        self.total_salary = self.total_salary + salary
        file = open(self.user_username + '.txt', 'a')
        file.write('\t'+ day + ':\n')
        file.write('\t\tTime in: ' + self.time_in + '\n')
        file.write('\t\tTime out: ' + self.time_out + '\t\t*******************\n')
        file.write('\t\tTime in ot: ' + self.time_in_ot + '\t*     '+ self.holiday() + '\t  *\n')
        file.write('\t\tTime out ot: ' + self.time_out_ot + '\t*******************\n')
        file.write('\t\tSalary: ' + str(round(salary, 2)) + '\n')
        file.close()
        self.resetTime()

    # another function for generating report /
    def generateDTRRecord3(self):
        total_less = (self.total_salary * 0.01) + (self.total_salary * 0.022)
        file = open(self.user_username + '.txt', 'a')
        file.write('\tLess:\n')
        file.write('\t\tPhil-health(1%): ' + str(round(self.total_salary * 0.01, 2)) + '\n')
        file.write('\t\tPag-ibig(2.2%): ' + str(round(self.total_salary * 0.022, 2)) + '\n')
        file.write('\t\tTotal less: ' + str(round(total_less, 2)) + '\n\n')
        file.write('\tTotal salary: ' + str(round(self.total_salary - total_less, 2)) + '\n')

    # function to save the salary whether holiday or not
    def getAppropriateSalary(self, salary):
        if self.isHoliday == True:
            return salary * 2
        return salary

    # get the word holiday if this day is holiday, otherwise NOT
    def holiday(self):
        if self.isHoliday == True:
            self.isHoliday = bool
            return "Holiday"
        self.isHoliday = bool
        return "  Not"
