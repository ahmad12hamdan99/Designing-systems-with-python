from datetime import datetime
from datetime import time
import os.path
import re
import pickle

class klassroom:
    '''
    this class define classroom in educational institution
    properties:
    - capacity: number of seats in the classroom
    - number: id number of the classroom
    - air_conditioner: a string value (yes/no) define if the classroom has air conditioner or not
    - activities : dictionary on activities assigned to this classroom: key:"activity name", value:[start_time,end_time]
    methods:
    - assign_activity: assign an activity to this classroom takes activity name, start time and end time as parameters
    - print: print summary of the classroom
    '''
    def __init__(self, capacity, number, air_conditioner):
        self._capacity = capacity
        self._number = number
        self._air_conditioner = air_conditioner
        self.activities = dict()

    @property
    def capacity(self):
        return self._capacity

    # a setter function
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def number(self):
        return self._number

    # a setter function
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def air_conditioner(self):
        return self._air_conditioner

    # a setter function
    @air_conditioner.setter
    def air_conditioner(self, air_conditioner):
        self._air_conditioner = air_conditioner


    def assign_activity(self, activity, start_time, end_time):
        '''
        assign an activity to classroom
        :param activity: activity name (string)
        :param start_time: start time of the activity in the form hh:mm
        :param end_time: end time of the activity in the form hh:mm
        '''
        if (start_time > time(21, 00, 00) or start_time< time(8, 00, 00))or(end_time >time(21, 00, 00) or end_time<time(8, 00, 00)):
            print("Sorry activities are allowed only during working hours from 08:00 till 21:00")
            return
        else:
            if (end_time >= start_time):
                for key in self.activities.keys():
                    if (start_time > self.activities[key][0] and start_time < self.activities[key][1]) or (end_time > self.activities[key][0] and end_time < self.activities[key][1]) or (start_time > self.activities[key][0] and end_time < self.activities[key][1])or (start_time < self.activities[key][0] and end_time > self.activities[key][1]):
                        print("sorry! the class is not available due to  overlap with another activity ")
                        return
                self.activities[activity] = [start_time, end_time]
                print("Activity added")
            else:
                print("invalid entry ")
                return


    def __str__(self):
        '''
        operator overloading of print function. print a summary of this classroom: number, capacity,air conditioner and
        a list of activities assigned to this classroom today
        :return: string
        '''
        str = ""
        str += f'class room number {self.number}, capacity {self.capacity}, air conditioner {self.air_conditioner}\n'
        if len(self.activities) !=0:
            str += "list of activities today:\n"
            for key in self.activities:
                str += f'{key} : from {(self.activities[key][0].hour):02d}:{(self.activities[key][0].minute):02d} to {(self.activities[key][1].hour):02d}:{(self.activities[key][1].minute):02d}\n'
            return str
        else:
            str += "No activities assigned to this class room"
            return str



class LectureAuditorium:
    '''
    this class define auditorium in educational institution
    properties:
    - capacity: number of seats in the auditorium
    - number: id number of the auditorium
    - air_conditioner: a string value (yes/no) define if the auditorium has air conditioner or not
    - activities : dictionary on activities assigned to this auditorium: key:"activity name", value:[start_time,end_time]
    methods:
    - assign_activity: assign an activity to this auditorium takes activity name, start time and end time as parameters
    - print: print summary of the auditorium
    '''
    def __init__(self, capacity, number, air_conditioner):
        self._capacity = capacity
        self._number = number
        self._air_conditioner = air_conditioner
        self.activities = dict()

    @property
    def capacity(self):
        return self._capacity

    # a setter function
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def number(self):
        return self._number

    # a setter function
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def air_conditioner(self):
        return self._air_conditioner

    # a setter function
    @air_conditioner.setter
    def air_conditioner(self, air_conditioner):
        self._air_conditioner = air_conditioner

    def assign_activity(self, activity, start_time, end_time):
        '''
        assign an activity to auditorium
        :param activity: activity name (string)
        :param start_time: start time of the activity in the form hh:mm
        :param end_time: end time of the activity in the form hh:mm
        '''
        if (start_time > time(21, 00, 00) or start_time< time(8, 00, 00))or(end_time >time(21, 00, 00) or end_time<time(8, 00, 00)):
            print("Sorry activities are allowed only during working hours from 08:00 till 21:00")
            return
        else:
            if (end_time >= start_time):
                for key in self.activities.keys():
                    if (start_time > self.activities[key][0] and start_time < self.activities[key][1]) or (end_time > self.activities[key][0] and end_time < self.activities[key][1]) or (start_time > self.activities[key][0] and end_time < self.activities[key][1])or (start_time < self.activities[key][0] and end_time > self.activities[key][1]):
                        print("sorry! the class is not available due to  overlap with another activity ")
                        return
                self.activities[activity] = [start_time, end_time]
                print("Activity added")
            else:
                print("invalid entry ")
                return


    def __str__(self):
        '''
        operator overloading of print function. print a summary of this classroom: number, capacity,air conditioner and
        a list of activities assigned to this classroom today
        :return: string
        '''
        str = ""
        str += f'auditorium number {self.number}, capacity {self.capacity}, air conditioner {self.air_conditioner}\n'
        if len(self.activities) !=0:
            str += "list of activities today:\n"
            for key in self.activities:
                str += f'{key} : from {(self.activities[key][0].hour):02d}:{(self.activities[key][0].minute):02d} to {(self.activities[key][1].hour):02d}:{(self.activities[key][1].minute):02d}\n'
            return str
        else:
            str += "No activities assigned to this auditorium"
            return str

class EdInstitution:
    '''
    this class define educational institution
    properties:
    - name: name of institution
    - classrooms: list of classrooms in the institution
    - lectureAuditoriums: list of auditoriums in the institution
    methods:
    - get_classroom: get classroom from the classrooms list by number
    - add_classroom: add classroom to the classrooms list
    - remove_classroom: remove classroom from the classrooms list
    - get_auditorium: get auditorium from the auditoriums list by number
    - add_auditorium: add auditorium to the auditoriums list
    - remove_auditorium: remove auditorium from the auditoriums list
    - saveToFile: save the institution object to pickle file
    - restoreFromFile: restore institution object from pickle file
    - print: print summary of the institution
    '''
    def __init__(self, name):
        self._name = name
        self.classrooms = []
        self.lectureAuditoriums = []

    @property
    def name(self):
        return self._name

    # a setter function
    @name.setter
    def name(self, name):
        self._name = name


    def get_classroom(self, number):
        '''
        get classroom from the classrooms list by number
        :param number: the number of the classroom
        :return: klassroom object
        '''
        for classR in self.classrooms:
            if classR.number == number:
                return classR
        print("there is no classroom with the specified number")
        return None

    def add_classroom(self, capacity, number, air_conditioner):
        '''
        add new classroom to the classrooms list in the institution
        :param capacity: capacity of the classroom
        :param number: the number of the classroom
        :param air_conditioner: a string value (yes/no) define if the classroom has air conditioner or not
        '''
        for classR in self.classrooms:
            if classR.number == number:
                print("there is a class room with same number already. try another number")
                return
        class_room = klassroom(capacity, number, air_conditioner)
        self.classrooms.append(class_room)
        print(f'Classroom successfully added to {self.name}')

    def remove_classroom(self, number):
        '''
        remove classroom from classrooms list in the institution
        :param number: the number of the classroom
        '''
        for classR in self.classrooms:
            if classR.number == number:
                self.classrooms.remove(classR)
                print(f'Classroom  successfully removed from {self.name}')
                return
        print("there is no classroom with the specified number")

    def get_auditorium(self, number):
        '''
        get auditorium from the auditoriums list by number
        :param number: the number of the auditorium
        :return: Auditorium object
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                return auditoriumR
        print("there is no auditorium with the specified number")
        return None

    def add_auditorium(self, capacity, number, air_conditioner):
        '''
        add new auditorium to the auditoriums list in the institution
        :param capacity: capacity of the auditorium
        :param number: the number of the auditorium
        :param air_conditioner: a string value (yes/no) define if the auditorium has air conditioner or not
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                print("there is a auditorium with same number already. try another number")
                return
        auditorium = LectureAuditorium(capacity, number, air_conditioner)
        self.lectureAuditoriums.append(auditorium)
        print(f'Auditorium successfully added to {self.name}')

    def remove_auditorium(self, number):
        '''
        remove auditorium from auditoriums list in the institution
        :param number: the number of the auditorium
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                self.lectureAuditoriums.remove(auditoriumR)
                print(f'Auditorium  successfully removed from {self.name}')
                return
        print("there is no auditorium with the specified number")

    def __str__(self):
        '''
        operator overloading of print function. print a summary of this institution: name, number of classrooms
        number of auditoriums and the number if available classrooms and auditoriums right now
        :return: string
        '''
        avaliable_classrooms = 0
        avaliable_auditoriums = 0
        str=""
        str += self.name+"\n"
        str += f'\t Classrooms: {len(self.classrooms)}\n'
        str += f'\t Auditorium(s): {len(self.lectureAuditoriums)}\n'
        now = datetime.now()
        flag1 = 1
        flag2 = 1
        if now.time()<time(8,00,00) or now.time()>time(21,00,00):
            avaliable_classrooms=0
            avaliable_auditoriums=0
        else:
            for classR in self.classrooms:
                if len(classR.activities) == 0:
                    avaliable_classrooms += 1
                else:
                    for key in classR.activities:
                        if now.time() > classR.activities[key][0] and now.time() < classR.activities[key][1]:
                            flag1 = 0
                    if flag1 == 1:
                        avaliable_classrooms += 1
                        flag1 = 0
            for auditoriumR in self.lectureAuditoriums:
                if len(auditoriumR.activities) == 0:
                    avaliable_auditoriums += 1
                else:
                    for key in auditoriumR.activities:
                        if now.time() > auditoriumR.activities[key][0] and now.time() < auditoriumR.activities[key][1]:
                            flag2 = 0
                    if flag2 == 1:
                        avaliable_auditoriums += 1
                        flag2 = 0

        str+=f'\t Status for today (now) : {avaliable_classrooms} available classroom(s) and {avaliable_auditoriums} available auditoriums(s))'
        return str

    def saveToFile(self):
        '''
        save institution object to pickle file
        '''
        with open(f'{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def restoreFromFile(self):
        '''
        restore institution object to pickle file
        '''
        if os.path.exists(f'{self.name}.pkl'):
            try:
                with open(f'{self.name}.pkl', 'rb') as f:
                    R= pickle.load(f)
                    return R
            except e:
                print(e)


# helper
def validate_input(input_type, value):
    '''
    valditer function to validate the input
    :param input_type: type of validation
    :param value: the input needed to validate
    :return: valid or not (bool)
    '''

    # validate in case of yes/no input
    if input_type == "decision":
        if value.lower() == "yes" or value.lower() == "no":
            return True
        else:
            print("input should be yes/no")
            return False

    # validate in case of 1 or 2 input
    if input_type == "choice1or2":
        if value.isdigit():
            if int(value) == 1 or int(value) == 2:
                return True
            else:
                print("input should be 1 or 2")
                return False
        else:
            print("input should be 1 or 2")
            return False

    # validate in case of choose between 1 and 5
    if input_type == "digit1to5":
        if value.isdigit():
            if int(value) in range(1, 6):
                return True
            else:
                print("input should be an integer between 1 and 5")
                return False
        else:
            print("input should be an integer between 1 and 5")
            return False

    # validate in case of time input in the form hh:dd
    if input_type=="time":
        regex = "^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
        p = re.compile(regex)
        if value == "":
            print("Invalid input, use the following form hh:mm")
            return False
        m = re.search(p, value)
        if m is None:
            print("Invalid input, use the following form hh:mm")
            return False
        else:
            return True


# define a list of institutions
institutions_list=[]
new_institution = EdInstitution("Innopolis University")
institutions_list.append(new_institution)

new_institution1 = EdInstitution("Kazan Federal University")
institutions_list.append(new_institution1)

# restore institutions data
for u in institutions_list:
    u.restoreFromFile()


run=1
chosen_institution=""
while(run):
    print("Choose one operation from below :")
    print("\t 1 : Add classroom or Auditorium to institution:")
    print("\t 2 : Print institution summary :")
    print("\t 3 : Assign activity to classroom :")
    print("\t 4 : Assign activity to LectureAuditorium :")
    print("\t 5 : Exit program")

    code=input()
    if validate_input("digit1to5",code):
        code=int(code)
    else:
        continue

    if code==1:
        print("Enter institution name :")
        chosen_institution=None
        institutions_name=input()
        for u in institutions_list:
            if u.name.lower() == institutions_name.lower():
                chosen_institution=u
                break
        if chosen_institution==None:
            print("No such a university in the database")
            continue
        print("Enter(classroom - 1 or Auditorium - 2):")
        c = input()
        while not validate_input("choice1or2",c):
            c=input()
        c=int(c)

        if c==1:
            loop_to_enter_classroom = 1
            while (loop_to_enter_classroom == 1):
                print("Enter (capacity, number, air conditioner- yes/no):")
                capacity, number, air_conditioner = input().split()
                while not capacity.isdigit() or not number.isdigit() or not validate_input("decision",air_conditioner):
                    if not capacity.isdigit():
                        print("capacity should be integer")
                    if not number.isdigit():
                        print("classroom number should be integer")
                    capacity, number, air_conditioner = input().split()

                chosen_institution.add_classroom(capacity,number,air_conditioner)
                print(f'Add another classroom {chosen_institution.name}? (yes/no)')

                decision = input()
                while not validate_input("decision", decision):
                    decision = input()

                if decision == "no":
                    loop_to_enter_classroom = 0
                else:
                    loop_to_enter_classroom = 1
        else:
            loop_to_enter_auditorium = 1
            while (loop_to_enter_auditorium == 1):
                print("Enter (capacity, number, air conditioner- yes/no):")
                capacity, number, air_conditioner = input().split()
                while not capacity.isdigit() or not number.isdigit() or not validate_input("decision",air_conditioner):
                    if not capacity.isdigit():
                        print("capacity should be integer")
                    if not number.isdigit():
                        print("auditorium number should be integer")
                    capacity, number, air_conditioner = input().split()
                chosen_institution.add_auditorium(capacity, number, air_conditioner)
                print(f'Add another auditorium {chosen_institution.name}? (yes/no)')
                decision=input()
                while not validate_input("decision", decision):
                    decision = input()

                if decision=="no":
                    loop_to_enter_auditorium=0
                else:
                    loop_to_enter_auditorium=1
    elif code==2:
        print("Enter institution name :")
        universitiy_name = input()
        for u in institutions_list:
            if u.name.lower() == universitiy_name.lower():
                chosen_institution = u
                break
        print(u)
    elif code==3:
        print("Choose classroom number:")
        classroom_n=(input())
        chosen_classroom=chosen_institution.get_classroom(classroom_n)
        if chosen_classroom != None:
            loop_to_enter_activity=1
            while(loop_to_enter_activity==1):
                print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
                activity_name, start_time, end_time = input().split()
                if not validate_input("time",start_time) or not validate_input("time",end_time):
                    activity_name, start_time, end_time = input().split()

                start_time_l=start_time.split(':')
                end_time_l=start_time.split(':')

                s = time(int(start_time_l[0]),int(start_time_l[1]), 00)
                e = time(int(end_time_l[0]),int(end_time_l[1]), 00)
                chosen_classroom.assign_activity(activity_name, s, e)
                print("Add another activity ? (yes/no)")
                decision = input()
                if decision == "no":
                    loop_to_enter_activity = 0
                    print(chosen_classroom)
                else:
                    loop_to_enter_activity = 1
    elif code ==4:
        print("Choose auditorium number:")
        auditorium_n = (input())
        chosen_auditorium = chosen_institution.get_auditorium(auditorium_n)
        if chosen_auditorium != None:
            loop_to_enter_activity = 1
            while (loop_to_enter_activity == 1):
                print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
                activity_name, start_time, end_time = input().split()
                start_time_l = start_time.split(':')
                end_time_l = start_time.split(':')

                s = time(int(start_time_l[0]), int(start_time_l[1]), 00)
                e = time(int(end_time_l[0]), int(end_time_l[1]), 00)
                chosen_auditorium.assign_activity(activity_name, s, e)
                print("Add another activity ? (yes/no)")
                decision = input()
                if decision == "no":
                    loop_to_enter_activity = 0
                    print(chosen_auditorium)
                else:
                    loop_to_enter_activity = 1

    elif code==5:
        print("Are you sure you want to exit")
        decision=input()
        while not validate_input("decision", decision):
            decision = input()
        if decision=="yes":
            run = 0
            for uni in institutions_list:
                print(uni)
                uni.saveToFile()
        else:
            continue
